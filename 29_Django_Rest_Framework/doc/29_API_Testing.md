### API Testing

Ref: [Testing](https://www.django-rest-framework.org/api-guide/testing/)

DRF included few helper classes extending Django's existing (`RequestFactory`) test framework and improve making API requests.

DRF's [`APIRequestFactory`](https://www.django-rest-framework.org/api-guide/testing/#apirequestfactory) class provides all standard request methods, that are `.get()`, `.post()`, `.patch()`, `.delete()`, `.head()`, `.options()`

Also, [`APIClient`](https://www.django-rest-framework.org/api-guide/testing/#apiclient) class extending Django's `Client` class, supports all standard methods.
This APIClient is used in [API Test case](https://www.django-rest-framework.org/api-guide/testing/#api-test-cases), which provides test case classes:
- APISimpleTestCase
- APITransctionTestCase
- APITestCase
- APILiveServerTestCase

Here, creating Test case for class `ProductDetailAPIView`, which accepts GET request to get individual detail object. Also accepts UPDATE and DESTROY request as it inherits `generics.RetrieveUpdateDestroyAPIView`.
We are going to test functionality alongside `get_permissions` method, that requires ADMIN user to send a PUT, PATCH or DELETE request, while other request like GET is allowed to any user.

Step 1: In "api/tests.py", import `from rest_framework.test import APITestCase` and create following class
```
class ProductAPITestCase(APITestCase):
    def setUp(self):
        self.admin_user = User.objects.create_superuser(username='admin', password='adminpass')
        self.normal_user = User.objects.create_user(username='user',password='userpass')
        self.product = Product.objects.create(
            name="Test Product",
            description="Test Description",
            price=9.99,
            stock=10
        )
        self.url = reverse('product-detail', kwargs={'product_id':self.product.pk})
```

*setUp() - defines common setup code that's going to run before each test case within this particular class
Since url pattern is `'products/<int:product_id>'`, it request a product_id, we call self.product.pk of above created product
`self.url` will send requests to that url to retrieve individual object allow to perform any of standard request method on that object.

Step 2: Name the url of product detail as `name='product-detail'` in urls.py
*It is good practice to use named urls to refer them in tests, here using reverse function

Step 3: Write test case function for GET request, which dont need authentication and has permmision allow anyone to request.
```
def test_get_product(self):
    response = self.client.get(self.url)
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.data['name'], self.product.name)
```

**Testing in terminal:
```> python .\manage.py test
Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.
----------------------------------------------------------------------
Ran 1 test in 2.023s

OK
Destroying test database for alias 'default'...
```

Step 4: Add test for unauthorized request to update product
```
def test_unauthorized_update_product(self):
    data = {"name": "Updated Product"}
    response = self.client.put(self.url, data)
    self.assertEqual(response.status_code, 401)
```
**Testing in terminal:
```> python .\manage.py test
Found 2 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..
----------------------------------------------------------------------
Ran 2 tests in 4.589s

OK
Destroying test database for alias 'default'...
```

Step 5: Replace status codes with status module of rest framework. 
`from rest_framework import status`
200 --> status.HTTP_200_OK
401 --> status.HTTP_401_UNAUTHORIZED

This is readable, explicit and industry standard

Step 6: Add delete test for unauthorised user
```
def test_unauthorized_delete_product(self):        
    response = self.client.delete(self.url)
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
```

**Run same testing cmd in terminal, should verify OK running 3 tests.

Step 7: Here, we test that user wont be able to delete product as delete permission allowed to only admin.
```
def test_only_admins_can_delete_product(self):
        # test normal user cannot delete - note that this could be its own method
        self.client.login(username="user", password='userpass')
        response = self.client.delete(self.url)     # expecting delete to fail here
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue(Product.objects.filter(pk=self.product.pk).exists())    # since delete fails, product must still exist in backend
```

** Testing in terminal:
```
Ran 4 tests in 10.006s

OK
```

Step 8: Within same above function, test for admin to able to delete product
```
def test_only_admins_can_delete_product(self):
    ...
    # test admin user can delete
    self.client.login(username="admin", password='adminpass')   # login: admin
    response = self.client.delete(self.url)     # expecting to delete the product
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)      # since product is deleted, there is no content
    self.assertFalse(Product.objects.filter(pk=self.product.pk).exists())    # since deleted the product, we dont expect product to exist in backened cache DB
```

***Exercise to try PUT and PATCH product test similar to the above delete

[Checking the response data](https://www.django-rest-framework.org/api-guide/testing/#checking-the-response-data)
While checking validity of test responses, its convenient to inspect the data that the response was created with, rather than inspecting the fully rendered response.
This can be done using `response.data`




