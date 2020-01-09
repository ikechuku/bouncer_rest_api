import json
from django.urls import reverse
from rest_framework import status 
from rest_framework.test import APITestCase
from .mock_data.forgot_password_data import customer_forgot_password_data, vendor_forgot_password_data, user1_registration_data, user2_registration_data, customer_registration_data, vendor_registration_data
from ..models.customer import Customer
from ..models.vendor import Vendor
from ..models.user import User


class BaseViewTest(APITestCase):
    def setUp(self):
        user = User.objects.create(**user1_registration_data())
        user.save()
        customer = Customer.objects.create(**customer_registration_data(), user=user)
        customer.save()
        
        user1 = User.objects.create(**user2_registration_data())
        user1.save()
        vendor = Vendor.objects.create(**vendor_registration_data(), user=user1)
        vendor.save()

class TestForgotPassword(BaseViewTest):

    def test_customer_forgot_password(self):
        url = reverse("forgot_password")
        response = self.client.post(url, customer_forgot_password_data())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_vendor_forgot_password(self):

        url = reverse('forgot_password')
        response = self.client.post(url, vendor_forgot_password_data())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
