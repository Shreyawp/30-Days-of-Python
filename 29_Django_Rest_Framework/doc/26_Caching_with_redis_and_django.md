### Caching with Redis and Django

Ref: [DRF Caching](https://www.django-rest-framework.org/api-guide/caching/)
[Redis](https://hub.docker.com/_/redis)
[Django Redis](https://docs.djangoproject.com/en/5.2/topics/cache/#redis)

Caching is an important way to improve the performance of apis and applies to Django or any other backened framework or language.
It caches data that doesn't commonly change and also cache data at busiest endpoints in order to improve API performance and reduce load on databases and server.

Here, using Redis as caching backend integrated with Django Rest Framework ViewSet actions.
Redis - is key:value database
      - provides cloud and on-prem solutions for caching, vector search and NoSQL DB
      - its stores data in memory or other persistant storage options.
      - perfect for cached backend in most producton settings.

Step 1: Will be using docker container to store redis cache. Run following cmds in terminal
>> $ docker run --name django-redis -d -p 6379:6379 --rm redis 
{ -d = detached mode, -p = port (allows host from Django app to connect to redis's database ), --rm = remove/cleanup docker container once stopped}
>> <container id>
>> $ docker ps
>> <shows running containers and above django-redis>
>> $ pip install "redis[hiredis]"
>> $ pip install django-redis

![alt text](media/26_docker_redis_image.PNG)

✔ Docker is running on your PC
✔ You created a container named django-redis
✔ Redis runs inside that container
✔ Redis stores cache as key:value
✔ -p 6379:6379 maps your PC port → container port
✔ When you hit API, Django stores cache in Redis

Step 2: In "settings.py" add following [django-redis config](https://github.com/jazzband/django-redis?tab=readme-ov-file#configure-as-cache-backend)
```
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
```

Step 3: In views.py, import following
```
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
...
class ProductListCreateAPIView(generics.ListCreateAPIView):
... pagination_class ...

    @method_decorator(cache_page(60 * 15, key_prefix='product_list'))
    # Response to any URL that is passed to this list method is going to be cached and that's gonna be stored in redis 
    # Every request to this page has different query string that is going to have different cache key 
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    # Responsible for fetching db objects for list view from db
    # But since we are using list method above, no need to hit db  cos we can immediately return response from redis cache
    def get_queryset(self):
        import time
        time.sleep(2)
        return super().get_queryset()

    def get_permissions()...
```

** Testing the browser endpoint /products/
- If refresh page, it takes 2 secs to return response and the reason for that is because get_queryset method is going to the DB which takes 2 secs
- Refesh again, notice it returns response immediately, cause the API response for this URL has been cached.
- This is now fast as it avoids the DB access and it avoids the 2 secs sleep from get_queryset method
In real case scenario, the query to DB could be performing a lot complex operations and joins and it might take while to complete that query and return data to the client. So CACHING allows to circumvent that and it allows to return response very quickly.
- @method_decorator is going to create different cache entry if the URL changes. Try changing url /products/?ordering=name and notice it take 2 secs as its new URL not cached previously. Each one of these url are going to be cached in Redis DB
- This helps improving performance, reducing the load on our server and DBs, while it only works with data that is relatively static and data that can be inaccurate for small amt of time.

For example : turn pagination off by changing "pagination_class = None"
If we refresh page, it returns same page that is previously cached, so it wont apply the pagination setting here until cache has timed out in our case to 15 mins. 
Otherwise, we can invalidate the cache and get back different response potentially containing new objects or removing deleted objects.
This way of caching is better if the new projects or orders are added or removed each day or week, but can be bad to cache if changed frequently in mins or hours.

Lets look at invalidation strategies. So if data changes and we want accurate results, the cache needs to be invalidate if things are added, updated or deleted. One way to do that is using Django signals.

Step 4: Add signals.py file in api/ and import signals post_save and post_delete, Django's receiver decoretor and cache object.
Now, setup function called invalidate_product_cache.
```
@receiver([post_save, post_delete], sender=Product)
def invalidate_product_cache(sender, instance, **kwargs):
    print("Clearing product cache")
```

This function is going to be called when post_save and post_delete signal is fired on Product model. In other words, when an instance of product model is saved or deleted after that action occurs, its going to call invalidate_product_cache function followed by a message, this will invalidate all of the cache objects that have key_prefix "product_list", i.e. remove all of these keys from cache and 

Once signals.py is created, we add ready() method in api/apps.py/class ApiConfig. Import signals module from current app. 
```
class ApiConfig(AppConfig):
    ...

    def ready(self):
        from . import signals
```

Then restart Django dev server at terminal.

Fact, Django redis backened has delete many function which takes wildcard and see how its going to be useful.

Step 5: Run following in terminal
>> docker ps
*Copy the container id

*access the container, open bash using above container id
>> docker exec -ti <container_id> bash
root@<container_id>:/data# redis-cli -n 1   {connects to redis db 1}
host:port[1]> KEYS *                        {Not recommended cmd in real projects as it blows up redis}

*There might be 2 cache_page decorator having "product_list" key_prefix
*Copy one of the keys
host:port[1]> GET "<key>"
host:port[1]> ...                          {returns cache response which is a string, this uses the browsable API response}
host:port[1]> exit             
root@<container_id>:/data# exit

![alt text](media/26_cache_KEYS.PNG)

Let's try to to invalidate the cache using delete_pattern and delete "product_list" keys from "KEYS *" cmd result
Checkout [delete_pattern](https://github.com/jazzband/django-redis?tab=readme-ov-file#scan--delete-keys-in-bulk) -- allows to delete all keys that contain particular pattern, using wildcard operator like ("foo_*")

Step 6: Add delete_pattern in signal.py 
`cache.delete_pattern('*product_list*')`

**Testing: run server , open browser endpoint 
Goto django admin/ API -> Products -> click on "Add product" -> fill details -> Save  

Goto /products/ , refresh page and view the product is added
Notice when page is refresh it takes a while since the cache was invalidated when added a new product
What actually happened is post_save is fired and followed by invalidate function call which deletes the cache pattern given.

Similarly, now delete the product from admin page, refresh the page and that shall take 2 secs again to cache. 
This fires post_delete signal and deletes the invalidated cache of "product_list" key.

One option while caching API responses is to use cache page decorator and that will create entry in cache for every distinct URL that ends up calling that particular view.
SO, if we add query parameter such as search, order to URL or pagination series parameter , they are all going to be cached separately, this is something one may or may not want, but that's the behaviour of the cache_page decorator in Django, not DRF.

Since cache_page is common key, it can delete any unwanted cache, we used delete_pattern to make sure to delete only "product_list*" pattern from Redis DB

Caching is complex topic but Django provides some useful utilities that integrate well with DRF, its important to consider what actually to cache in application. 
Anything that changes a lot is not good for caching but data that is relatively static and can be out-of-date for small period of time, these are good options for caching and can improve performance of the API, and can also reduce the load on DB


Sometimes, one wants JSON format in browsable API, this too gets cached but instead of html response its a json string, if we lookup redis db using bash as above.

