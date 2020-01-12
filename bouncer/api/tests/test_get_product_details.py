import json
from django.urls import reverse
from rest_framework import status 
from rest_framework.test import APITestCase
from .mock_data.forgot_password_data import *
from .mock_data.product_data import product_data, test_product_data
from .mock_data.category_data import category_data
from ..models.customer import Customer
from ..models.vendor import Vendor
from ..models.user import User
from ..models.category import Category
from ..models.product import Product


class BaseViewTest(APITestCase):
    def setUp(self):
        user = User.objects.create(**user2_registration_data())
        user.save()
        vendor = Vendor.objects.create(**vendor_registration_data(), user=user)
        vendor.save()
        cat = Category.objects.create(**category_data())
        cat.save()
        self.product = Product.objects.create(**product_data(), category_id=cat, vendor_id=vendor)
        self.product.save()
        return 

class TestGetProductDetails(BaseViewTest):
    def test_get_product_details(self):
        url = reverse('get_product_details', kwargs={"id":1})
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
