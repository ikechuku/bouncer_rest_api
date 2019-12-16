from decouple import config
import sys
sys.path.append("..")
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ...utils.helper import random_string_generator
from ...serializers.userSerializers import UserSerializers
from ...serializers.vendorSerializer import VendorSerializers
from ...models.user.users import User
from ...models.user.vendor import Vendor
import bcrypt
from django.core.mail import send_mail,EmailMessage

class VendorRegistration(APIView):

    def post(self, request):
        data = request.data
    
        hashed = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
        token = random_string_generator()
        user = User.objects.create(
            user_name = data['user_name'],
            password = hashed,
            token = token,
            is_vendor = True,
            email = data['email']
        )
        
        user.save()

        vendor = Vendor.objects.create(
            user = user,
            shop_name = data['shop_name'],
        )
        
        vendor.save()

        message = "Registration was successful"
        vendor = {
            "shop_name":data['shop_name'],
            "user_name":data['user_name'],
            "email":data['email'],
            "email_verified": False,
            "account_verified": False
        }

        subject = 'Bouncer email verification'

        text_content= "Welcome on board."

        to = [data["email"]]
        from_email = config("EMAIL_SENDER")
        
        html_content ='Welcome on board, complete your registration by clicking the link below'
        messages = f'Welcome on board </br> Click on this <a href="http://example.com/{token}">Link</a> to verify'

        msg= send_mail(subject, html_content,from_email,to, fail_silently=False,  html_message=messages)

        if msg:
            return Response({"message":message,"vendor":vendor},status=status.HTTP_201_CREATED)
        return Response({"message":"Error in delivering email"},status=status.HTTP_400_BAD_REQUEST)

    