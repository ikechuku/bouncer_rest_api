import sys
sys.path.append('..')
import json
from rest_framework import status 
from rest_framework.test import APITestCase, APIClient


class CustomerTest(APITestCase):
    client=APIClient()

    def test_post(self):
        data = {
            "last_name": "good",
            "first_name": "gooder",
            "email": "olatundesodiqs@gmail.com",
            "user_name": "ola",
            "password": "hello",
            "is_customer": True,
            "token": "hjfdsjkfl3"
        }

        url = '/api/customer/register/'
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(response.data['customer']['last_name'], 'good')