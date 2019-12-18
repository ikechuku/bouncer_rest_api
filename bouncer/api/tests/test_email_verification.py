import json
from .mock_data.registration_data import user_registration_data
from rest_framework import status 
from rest_framework.test import APITestCase
from ..models.user import User

class TestEmailVerification(APITestCase):
    
    def test_verify(self):
        user = User.objects.create(**user_registration_data())
        token = user.email_verification_token
        url = '/api/auth/verify-email/'
        response =self.client.post(url,{"email_verification_token":token})
        self.assertEqual(response.status_code,status.HTTP_202_ACCEPTED)
        self.assertEqual(response.data['message'], 'verified')
