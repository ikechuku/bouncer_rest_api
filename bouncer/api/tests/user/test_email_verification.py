import sys
sys.path.append('..')
import json
from ...tests.mock_data.user_setup import user_data
from rest_framework import status 
from rest_framework.test import APITestCase
from ...models.user.users import User

class EmailVerificationTest(APITestCase):
    
    def test_verify(self):
        create_url = '/api/customer/register/'
        user_create=self.client.post(create_url,user_data)
        user = User.objects.get(user_name=user_create.data['customer']['user_name'])
        token = user.token
        url = '/api/auth/verify-email/'
        response =self.client.post(url,{"token":token})
        self.assertEqual(response.status_code,status.HTTP_202_ACCEPTED)
        self.assertEqual(response.data['message'], 'verified')
