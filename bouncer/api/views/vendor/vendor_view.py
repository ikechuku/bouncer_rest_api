from decouple import config
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ...utils.helper import random_string_generator
from ...models.user import User
from ...models.vendor import Vendor
import bcrypt
from django.core.mail import send_mail,EmailMessage
from ...verification.vendor_validator import validate 
from ...utils.helper import  random_string_generator, send_email, vendor_message


class VendorRegistration(APIView):

    def post(self, request):
        data = request.data
        validate_data = validate(data, User, Vendor)
        
        if validate_data != True:
            return validate_data
        else:
            
            #hash user password using bycrpt algorithm
            hashed = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
            
            #generate token
            token = random_string_generator()
            
            #create user
            user = User.objects.create(
                user_name = data['user_name'],
                password = hashed,
                email_verification_token = token,
                user_type = 'vendor',
                )
        
            #create vendor
            vendor = Vendor.objects.create(
                user = user,
                shop_name = data['shop_name'],
                email = data['email']
                )
                
            user.save()
            
            #save vendor in database
            vendor.save()

            email_verification_url = config("VERIFY_EMAIL_URL")
            message = "Registration was successful"

            customer_message_details = {
                'subject': 'Bouncer email verification',
                'text_content': "You are welcome on board.",
                'to': [data["email"]],
                'from_email': config("EMAIL_SENDER"),
                'html_content': 'Welcome on board, complete your registration by clicking the link below',
                'link_message': f'Welcome on board </br> Click on this <a href="{email_verification_url}/?token={token}">Link</a> to verify'

            }

            # send mail to the user
            send = send_email(customer_message_details)
            if send:
                return Response({'message': message, 'user_message': vendor_message(data)}, status=status.HTTP_201_CREATED)
            else:
                return Response(dict(message='Network Error: Could not send email at the moment You are registered'), status=status.HTTP_503_SERVICE_UNAVAILABLE)
                