from decouple import config
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ...utils.helper import random_string_generator
from ...serializers.user_serializer import UserSerializer
from ...serializers.customer_serializer import CustomerSerializer
from ...models.user import User
from ...models.customer import Customer
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
            user_type = 'customer',
        )
        user.save()

        customer = Customer.objects.create(
            user = user,
            first_name = data['first_name'],
            last_name = data['last_name'],
            email = data['email']
        )
        customer.save()

        message = "Registration was successful"
        customer={
            "first_name":data['first_name'],
            "last_name":data['last_name'],
            "user_name":data['user_name'],
            "email":data['email'],
        }

        subject = 'Bouncer email verification'

        text_content= "Welcome on board."

        to = [data["email"]]
        from_email = config("EMAIL_SENDER")
        
        html_content ='Welcome on board, complete your registration by clicking the link below'
        link_message = f'Welcome on board </br> Click on this <a href="http://example.com/{token}">Link</a> to verify'

        msg= send_mail(subject, html_content,from_email,to, fail_silently=False,  html_message=link_message)

        if msg:
            return Response({"message":message,"customer":customer},status=status.HTTP_201_CREATED)
        return Response({"message":"Error in delivering email"},status=status.HTTP_400_BAD_REQUEST)
