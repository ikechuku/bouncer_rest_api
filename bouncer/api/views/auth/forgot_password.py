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
                print(email)
            elif user_type == "vendor":
                user = Vendor.objects.get(user_id=user_id)
                email = user.email

            user.token = token
            user.save()

                # try:
                #     # user = User.objects.get(user_name=data["user_name"])
                #     user.token = token
                #     user.save()
        except:

            return Response(dict(error="This user_name does not exist"), status=status.HTTP_400_BAD_REQUEST)

        subject = 'Bouncer Password Reset'

        to = [email]
        from_email = config("EMAIL_SENDER")
        
        html_content ='Complete your password reset by clicking the link below'
        link_message = f'Reset your password </br> Click on this <a href=" http://127.0.0.1:8100/auth/reset-password?{user_id} ">Link</a> to set a new password'
        message = "A password reset Link has been sent to your Email address"
        msg= send_mail(subject, html_content,from_email,to, fail_silently=False,  html_message=link_message)
        user={
            "user_id":user_id,
            "user_type":user_type,
            "user_name":user_name
        }

        if msg:
            return Response({"message":message, "user":user},status=status.HTTP_200_OK)
        return Response({"message":"Error in delivering email"},status=status.HTTP_400_BAD_REQUEST)