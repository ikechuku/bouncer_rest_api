import sys
sys.path.append('..')
import json
from rest_framework import status 
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse


class VendorTest(APITestCase):
    # client=APIClient()

    def setup(self):
        self.vendor = {
            "shop_name": "best4less",
            "email": "bamibabson@gmail.com",
            "user_name": "tunde",
            "password": "pass",
            "is_customer": True,
            "token": "fghtres"
        }
        
        
        
    def test_register_vendor(self):
        url = ('vendor_register')
        response = self.client.post(url, self.vendor, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['vendor']['shop_name'], 'best4less')
        