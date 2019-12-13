import json
from ..mock_data.user_setup import user_data
from rest_framework import status 
from rest_framework.test import APITestCase
from ...models.user.users import User

class TestEmailVerification(APITestCase):
    
    def test_verify(self):
        user = User.objects.create(**user_data)
        token = user.token
        url = '/api/auth/verify-email/'
        response =self.client.post(url,{"token":token})
        self.assertEqual(response.status_code,status.HTTP_202_ACCEPTED)
        self.assertEqual(response.data['message'], 'verified')
