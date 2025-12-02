## Adding Serializers and Response Object

Miscellaneous step:
Add 'rest_framework' to INSTALLED_APPS in settings.py

### Creating serializers.py and adding serializers
Step 1: Create new file 'serializers.py' in 'api/' 
** [Serializers](https://www.django-rest-framework.org/api-guide/serializers/#serializers) coverted django models and querysets to json data, and can deserialize the json data back to django models and querysets
** works similar to django's Form and ModelForm classes, Provides serializers and ModelSerializer class.

Step 2: Adding model-class Product to serializers.py and inherit the ModelSerializer.
Create inner-meta class, tie the model Product to meta class and specify fields that want to serialize to json
So, price field dont want it to be 0 or less than 0 , as it wont make sense. Thus, add [validation function](https://www.django-rest-framework.org/api-guide/serializers/#field-level-validation) validate_price

Step 3: Add function-based views 'product_list' in 'api/views.py' .
products --> fetch products from db using orm query 
serializer --> instantiate the ProductSerialzer(products, many=True), parameters products here are objects that converts to json and since there are more than one object set 'many' keyword-arg  to true (otherwise not needed for single object)
return JsonResponse --> reurning the dictionary of data 

Step 4: Add url path in 'api/urls.py' to view the product_list
** run server to view that the data is presented in json with url 'localhost:8000/products/'
** try removing 'description' field from serilizers.py and refresh page , verify that field is removed.

Will later look more about [Serializer Fields](https://www.django-rest-framework.org/api-guide/fields/#serializer-fields)

### Adding Response objects
Step 1: Import [Response object](https://www.django-rest-framework.org/api-guide/responses/#response) and api_view in 'api/views.py'
add [@api_view decorator](https://www.django-rest-framework.org/api-guide/views/#api_view) to product_list with "GET" arg
replace JsonResponse to Django Response object passing serializer.data arg
** Refresh the webpage and view that the look of webpage is changed to DRF Browsable API
Adding ['?format=json'](https://www.django-rest-framework.org/topics/browsable-api/#formats) in url to view the raw json format, we saw earlier.
url = 'localhost:8000/products/?format=json'

More about [BrowsableAPIRenderer](https://www.django-rest-framework.org/api-guide/renderers/#browsableapirenderer)

Step 2: Add 'id' to serialiers , which is an implicit field added as primary key 

Step 3: add url path for primary key to view product's detail of that 'id' 

Step 4: add function view 'product_detail' with following variables
product --> get only one object from Product model to lookup and get product based on pk arg otherwise gives '404 page not found' error (this is django model object)
serializer --> use same model serializer as product_list 
return Response remains same
** Verify the brower for url 'localhost:8000/products/1' and other ids, showing product detail

