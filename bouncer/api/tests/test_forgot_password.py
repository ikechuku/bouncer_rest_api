import json
from django.urls import reverse
from rest_framework import status 
from rest_framework.test import APITestCase
from .mock_data.forgot_password_data import customer_forgot_password_data, vendor_forgot_password_data, create_customer, create_vendor
from ..models.customer import Customer
from ..models.vendor import Vendor
from ..models.user import User

class TestForgotPassword(APITestCase):

    def test_customer_forgot_password(self):
        create_customer()
      
        url = reverse("forgot_password")
        response = self.client.post(url, customer_forgot_password_data())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_vendor_forgot_password(self):
        create_vendor()
        url = reverse('forgot_password')
        response = self.client.post(url, vendor_forgot_password_data())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
