import json
from django.urls import reverse
from rest_framework import status 
from rest_framework.test import APITestCase, APIClient
from .mock_data.registration_data import vendor_registration_data


class TestVendor(APITestCase):

    def test_post(self):
        url = reverse('vendor_register')
        response = self.client.post(url, vendor_registration_data())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['user_message']['shop_name'], 'best4less')
        