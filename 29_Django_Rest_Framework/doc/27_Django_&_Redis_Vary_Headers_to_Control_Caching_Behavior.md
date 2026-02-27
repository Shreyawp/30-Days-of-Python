### Django & Redis - Vary Headers to Control Caching Behavior

Ref: [Vary Headers](https://docs.djangoproject.com/en/5.2/topics/http/decorators/#vary-headers)

Vary Headers are used to control caching based on request headers.

Step 1: Add the decorator in class OrderViewSet
```
@method_decorator(cache_page(60 * 15, key_prefix='order_list'))
def list(self, request, *args, **kwargs):
    return super().list(request, *args, **kwargs)
```

** Testing in api.http 
- check docker is running 
- Generate access token of user
- Send GET request to orders/ with authorized user
- Now if we change user1 to GET request, notice that response contain information of user2 as it was cached due to use of cache_page decorator in OrderViewSet
![alt text](media/27_before_header_vary.PNG)

The cache decorator will cache for evey DISTINCT url, while here the user authentication is on backend where its looks up authenticated user and that means for subsequent request, we get the wrong response.
Here, we need to distingush between different users sending the request and only cache based on request headers ("authorization")

Step 2: Add below after cache_page decorator 
`@method_decorator(vary_on_headers("Authorization"))`
and 
 `from django.vi ews.decorators.vary import vary_on_headers`

using vary headers, to define which request headers a cache meachanism should take into account when it build the cache key. for example, if contents of page depends on user's language preference, that will vary on language.

**Before testing, flush the cached data from redis. Run following on terminal
>> docker ps
>> docker exec -ti <container_id> bash
>> redis-cli -n -1
>> KEYS *
>> flushdb

*check if db is empty
>> KEYS *
*exit cli and container

**Testing in api.http
- using user1 send GET request to orders/, this will be cached on redis
- now, change token to user2 and send request, notice the response is user2 unlike before.
![alt text](media/27_after_header_vary.PNG)

Unlike before, we are getting different response for each user and that's because of vary_on_headers decorator. 
Its going to look at HTTP request of "authorization" header and if the value is different, its not going to use cached version, instead its going to return response and cache that specific response based on the authorization header. 
So the caching is user sepcific because of vary_header and once its cached the subsequent requests that have the same value for this key are going to use that cache to return their responses.


Now, one issue to address is that token used in authorization header might change frequently and that might result in lot of different caches being created for same user.

That depends on lifetime of JWT token, when that token expires it going to be recycled.
Lets set the lifetime of access and refresh tokens. 

Step 3: Add SIMPLE_JWT in settings.py
```
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}
```


