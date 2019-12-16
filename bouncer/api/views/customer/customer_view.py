from django.core.mail import send_mail,EmailMessage

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import bcrypt
from decouple import config

from ...serializers.user_serializer import UserSerializer
from ...serializers.customer_serializer import CustomerSerializer
from ...models.user import User
from ...models.customer import Customer

from ...utils.helper import  * 
from ...verification.customer_validator import *

class CustomerRegistration(APIView):

    def post(self, request):
        data = request.data
        validate_data = validate(data, User, Customer)

        if (validate_data != True):
            return validate_data
        else:   
            # hash user password using bcrypt algorithm
            hashed = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
            
            # Generate token
            token = random_string_generator()

            # create user 
            user = User.objects.create(
                user_name = data['user_name'].strip(),
                password = hashed,
                token = token,
                user_type = 'customer',
            )

            # create customer
            customer = Customer.objects.create(
                user = user,
                first_name = data['first_name'],
                last_name = data['last_name'],
                email = data['email']
            )

            message = "Registration was successful"
            def customer_message(data):
                return {
                "first_name":data['first_name'],
                "last_name":data['last_name'],
                "user_name":data['user_name'].strip(),
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
                # saue user in database
                user.save()
                # save customer in database
                customer.save()
                # return a valid response
                return Response({"message":message,"customer":customer_message(data)},status=status.HTTP_201_CREATED)
            # return an error message
            return Response({"message":"Error in delivering email"},status=status.HTTP_400_BAD_REQUEST)
