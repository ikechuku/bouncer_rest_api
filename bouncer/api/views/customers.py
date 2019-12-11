import sys
sys.path.append("..")
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..utils.helper import random_string_generator
from ..serializers.userSerializers import UserSerializers
from ..serializers.customerSerializer import CustomerSerializers
from ..models.users import User
from ..models.customers import Customers
import bcrypt
from django.core.mail import send_mail,EmailMessage

class CustomerRegistration(APIView):

    def post(self, request):
        data = request.data
    
        hashed = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
        token = random_string_generator()
        user = User.objects.create(
            user_name = data['user_name'],
            password = hashed,
            token = token,
            is_customer = True,
            email = data['email']
        )
        user.save()

        customer = Customers.objects.create(
            user = user,
            first_name = data['first_name'],
            last_name = data['last_name']
        )
        customer.save()

        message = "Registration was successful"
        customer={
            "first_name":data['first_name'],
            "last_name":data['last_name'],
            "user_name":data['user_name'],
            "email":data['email'],
            "token":token
        }

        subject = 'Bouncer email verification'

        text_content= "Welcome on board."

        to = [data["email"]]

        from_email = "adamstemii@gmail.com"
        
        html_content ='Welcome on board, complete your registration by clicking the link below'

        msg= send_mail(subject, html_content,from_email,to, fail_silently=True,  html_message='<a href=localhost:8100/email_verify/>link</a>')

        if msg:
            return Response({"message":message,"customer":customer},status=status.HTTP_201_CREATED)
        return Response({"message":"Error in delivering email"},status=status.HTTP_400_BAD_REQUEST)

    