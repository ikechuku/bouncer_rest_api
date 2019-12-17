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
                token = token,
                user_type = 'vendor',
                )
        
            #create vendor
            vendor = Vendor.objects.create(
                user = user,
                shop_name = data['shop_name'],
                email = data['email']
                )
            

            message = "Registration was successful"
            
            def vendor_message(data):
                return {
            "shop_name":data['shop_name'],
            "user_name":data['user_name'].strip(),
            "email":data['email'],
            "email_verified": False,
            "account_verified": False
            }
            

            subject = 'Bouncer email verification'

            text_content= "Welcome on board."

            to = [data["email"]]
            from_email = config("EMAIL_SENDER")
        
            html_content ='Welcome on board, complete your registration by clicking the link below'
            link_message = f'Welcome on board </br> Click on this <a href="http://example.com/{token}">Link</a> to verify'

            msg= send_mail(subject, html_content, from_email, to, fail_silently=False,  html_message=link_message)

            if msg:
                #save user in database
                user.save()
                
                #save vendor in database
                vendor.save()
                
                return Response({"message":message,"vendor":vendor_message(data)}, status=status.HTTP_201_CREATED)
            
            return Response({"message":"Error in delivering email"}, status=status.HTTP_400_BAD_REQUEST)
            
