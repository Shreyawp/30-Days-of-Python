from django.urls import reverse
from api.models import User, Product
from rest_framework.test import APITestCase
from rest_framework import status


# Create your tests here.
class ProductAPITestCase(APITestCase):
    def setUp(self):
        # Create new test admin with username and password parameters/keyword arguments
        self.admin_user = User.objects.create_superuser(username='admin', password='adminpass')
        self.normal_user = User.objects.create_user(username='user',password='userpass')
        self.product = Product.objects.create(
            name="Test Product",
            description="Test Description",
            price=9.99,
            stock=10
        )
        # Create url object to send request using reverse() with url_name and product_id arguments
        self.url = reverse('product-detail', kwargs={'product_id':self.product.pk})

    def test_get_product(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.product.name)

    def test_unauthorized_update_product(self):
        data = {"name": "Updated Product"}
        response = self.client.put(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unauthorized_delete_product(self):        
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_only_admins_can_delete_product(self):
        # test normal user cannot delete - note that this could be its own method
        self.client.login(username="user", password='userpass')     # login: user
        response = self.client.delete(self.url)     # expecting delete to fail here
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)       # since user dont have DELETE permission, the action is forbidden
        self.assertTrue(Product.objects.filter(pk=self.product.pk).exists())    # since delete fails, product must still exist in backend

        # test admin user can delete
        self.client.login(username="admin", password='adminpass')   # login: admin
        response = self.client.delete(self.url)     # expecting to delete the product
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)      # since product is deleted, there is no content
        self.assertFalse(Product.objects.filter(pk=self.product.pk).exists())    # since deleted the product, we dont expect product to exist in backened cache DB

    def test_admin_update_product(self):
        self.client.login(username="admin", password='adminpass')   # login: admin
        data = {"name": "Updated Product", 
                "description": "Updated Description",
                "price": "9.99",
                "stock": "10"   }       # PUT request must include all fields mentioned as in model, even if few field values remains same
        response = self.client.put(self.url, data)      # send PUT request to url with data
        self.assertEqual(response.status_code, status.HTTP_200_OK)      # Update reponse should be 200 for success
        self.product.refresh_from_db()      # Must refresh backend DB to ensure updates for following checks
        self.assertEqual(self.product.name, "Updated Product")      # verify if product name is updated in DB as given data

    def test_admin_patch_product(self):
        self.client.login(username="admin", password='adminpass')   # login: admin
        data = {"name": "Patched Product"}      # PATCH request only needs required field(s) to update
        response = self.client.patch(self.url, data)      # send PATCH request to url with data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.product.refresh_from_db()      # Must refresh backend DB to ensure updates for following checks
        self.assertEqual(self.product.name, "Patched Product")      # verify if product name is updated in DB as given data