from django.urls import reverse

from rest_framework import status 
from rest_framework.test import APIClient, APITestCase


class TestProductList(APITestCase):

    def test_product_list(self):

        url = reverse('product_list')
        response = self.client.get(url)

        self.assertEqual(type(response.data), type({}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
