import sys
import json
sys.path.append('..')

from django.urls import reverse
from rest_framework import status 
from rest_framework.test import APITestCase, APIClient

from ...tests.mock_data.customer_data import MockData

class CustomerTest(APITestCase):

    def test_post(self):
        url = reverse('customer_register')
        response = self.client.post(url, MockData.customer_data())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(response.data['customer']['last_name'], 'good')