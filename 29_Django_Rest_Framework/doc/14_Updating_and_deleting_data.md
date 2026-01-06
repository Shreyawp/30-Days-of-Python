### Updating and deleting data

Reference doc for [RetrieveUpdateDestroyAPIView](https://www.django-rest-framework.org/api-guide/generic-views/#retrieveupdatedestroyapiview)

Step 1: Replace class RetrieveAPIView to RetrieveUpdateDestroyAPIView in `api/views/class ProductDetailAPIView` 
Test in api.http with request ```GET http://localhost:8000/products/1 HTTP/1.1```
>> Response shows product details having id=1 

Step 2: Test with PUT request 
```
PUT http://localhost:8000/products/1 HTTP/1.1
Content-Type: application/json

{
    "name": "Television",
    "price": 300.00,
    "stock": 14,
    "description": "An amazing new TV"
}
```
It shall update the product where id = 1. 
Send GET request to the product id again to view updated product.

Step 3: Testing DELETE request in api.http
DELETE http://localhost:8000/products/1 HTTP/1.1

This will delete the product with response 204 No Content.
Sending GET request again, will respond 404 not found for product id = 1

Step 4: Adding the authorization to class ProductDetailAPIView
Test to get product_id 2 > it will get the product detail
Test delete request > should not give permission to delete as unauthorized.
Also, testing the put request will not allow updating product unauthorized.

cannot perform any of the http request ['PUT', 'PATCH', 'DELETE'] as permitted to admin in view class, without giving the authorization.

Now, lets add the Authorization to PUT request with access token and send equest to update.
```Authorization: Bearer < access token >```
This should work for authorized admin and show the updated product in response.


