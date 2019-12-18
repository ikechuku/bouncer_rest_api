import json
from django.urls import reverse
from rest_framework import status 
from rest_framework.test import APITestCase
from .mock_data.registration_data import forgot_password_customer_registration_data, forgot_password_vendor_registration_data
from .mock_data.forgot_password_data import customer_forgot_password_data, vendor_forgot_password_data
from ..models.customer import Customer
from ..models.vendor import Vendor
from ..models.user import User

class TestForgotPassword(APITestCase):

    def test_customer_forgot_password(self):
        
        user = User.objects.create(user_name= "customerDoe", password="pass123", user_type="customer", email_verified=False)
        Customer.objects.create(last_name= "Doe", email="customer@gmail.com", first_name="customer", user=user)
        url = reverse("forgot_password")
        response = self.client.post(url, customer_forgot_password_data())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_vendor_forgot_password(self):
        user = User.objects.create(user_name= "vendorDoe", password="pass123", user_type="vendor", email_verified=False)
        vendor = Vendor.objects.create(shop_name= "Doe", email="vendor@gmail.com", account_verified=False, user=user)

        url = reverse('forgot_password')
        response = self.client.post(url, vendor_forgot_password_data())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
