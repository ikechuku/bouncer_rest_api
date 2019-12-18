import json
from django.urls import reverse
from rest_framework import status 
from rest_framework.test import APITestCase
from .mock_data.auth_data import reset_password_data
from .mock_data.registration_data import customer_registration_data
from ..models.user import User
import bcrypt

class TestResetPassword(APITestCase):
    def setUp(self):
        data = customer_registration_data()
        hashed = bcrypt.hashpw(
            data['password'].encode('utf-8'), bcrypt.gensalt())
        token = 'sometoken'
        user = User.objects.create(
            user_name=data['user_name'],
            password=hashed,
            forgot_password_token=token,
            user_type='customer',
        )
        user.save()

    def test_user_reset_password(self):
        url = reverse("reset_password")
        response = self.client.post(url, reset_password_data())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        