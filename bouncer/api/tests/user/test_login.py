import sys
sys.path.append('..')
from rest_framework import status
from ...tests.mock_data.login_data import register_data, login_data
from rest_framework.test import APITestCase
from django.urls import reverse



class LoginTest(APITestCase):
    def setUp(self):
        url = reverse('customer_register')
        self.client.post(url, register_data())

    def test_login(self):
        url = reverse('login')
        response = self.client.post(url, login_data())

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "Login was successful")
