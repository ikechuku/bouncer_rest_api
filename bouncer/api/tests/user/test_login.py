from rest_framework import status
from ...tests.mock_data.login_data import register_data, auth_data
from rest_framework.test import APITestCase
from django.urls import reverse
from django.urls import reverse

from ...models.user.users import User
import bcrypt


class LoginTest(APITestCase):
    def setUp(self):
        data = register_data()
        hashed = bcrypt.hashpw(
            data['password'].encode('utf-8'), bcrypt.gensalt())
        token = 'sometoken'
        user = User.objects.create(
            user_name=data['user_name'],
            password=hashed,
            token=token,
            user_type='customer',
        )
        user.save()

    def test_login(self):
        url = reverse('login')
        response = self.client.post(url, auth_data())

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "Login was successful")
