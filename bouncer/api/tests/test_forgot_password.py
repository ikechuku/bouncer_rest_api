import json
from django.urls import reverse
from rest_framework import status 
from rest_framework.test import APITestCase, APIClient
from .mock_data.registration_data import fp_customer_registration_data, fp_vendor_registration_data, customer_registration_data, vendor_registration_data
from .mock_data.forgot_password_data import customer_forgot_password_data, vendor_forgot_password_data

class TestForgotPassword(APITestCase):

    def test_customer_forgot_password(self):
        reg_url = reverse("customer_register")
        response = self.client.post(reg_url, fp_customer_registration_data())

        url = reverse("forgot_password")
        response = self.client.post(url, customer_forgot_password_data())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['user']["email"], "johnDoe@gmail.com")


    def test_vendor_forgot_password(self):
        reg_url = reverse("vendor_register")
        response = self.client.post(reg_url, fp_vendor_registration_data())

        url = reverse('forgot_password')
        response = self.client.post(url, vendor_forgot_password_data())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['user']['email'], "anothertest@gmail.com")
