from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view,permission_classes
from ...models.user import User
from ...models.customer import Customer
from ...models.vendor import Vendor
from django.core.mail import send_mail,EmailMessage
from decouple import config
from ...utils.helper import random_string_generator


class ForgotPassword(APIView):
    def post(self, request):
        data = request.data
        token = random_string_generator()
        try:
            user_name=data['user_name']
            _user = User.objects.get(user_name = user_name)
            user_id = _user.id
            user_type = _user.user_type

            if user_type=="customer":
                user = Customer.objects.get(user_id=user_id)
                email = user.email   

            elif user_type == "vendor":
                user = Vendor.objects.get(user_id=user_id)
                email = user.email

            user.token = token

        except:

            return Response(dict(error="This user_name does not exist"), status=status.HTTP_400_BAD_REQUEST)

        subject = 'Bouncer Password Reset'

        to = [email]
        from_email = config("EMAIL_SENDER")
        
        html_content ='Complete your password reset by clicking the link below'
        link_message = f'Reset your password </br> Click on this <a href="http://bouncer-restapi-staging.herokuapp.com/api/auth/reset-password?{token} ">Link</a> to set a new password'
        message = "A password reset Link has been sent to your Email address"
        msg= send_mail(subject, html_content,from_email,to, fail_silently=False,  html_message=link_message)
        user_details={
            "user_id":user_id,
            "user_type":user_type,
            "user_name":user_name,
            "email": email
        }

        if msg:
            user.save()
            return Response({"message":message, "user":user_details},status=status.HTTP_200_OK)
        return Response({"message":"Error in delivering email"},status=status.HTTP_400_BAD_REQUEST)
        