import json

from django.urls import reverse
from rest_framework import status 
from rest_framework.test import APITestCase, APIClient

from .mock_data.registration_data import customer_registration_data

class TestCustomer(APITestCase):

    def test_post(self):
        url = reverse('customer_register')
        response = self.client.post(url, customer_registration_data())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['user_message']['last_name'], 'test')