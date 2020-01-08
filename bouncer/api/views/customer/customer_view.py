from django.core.mail import send_mail

from rest_framework.views import APIView

import bcrypt
from decouple import config

from ...models.user import User
from ...models.customer import Customer
from ...utils.helper import random_string_generator, send_email, customer_message
from ...verification.customer_validator import *


class CustomerRegistration(APIView):

    def post(self, request):
        data = request.data
        validate_data = validate(data, User, Customer)

        if (validate_data != True):
            return validate_data
        else:
            # hash user password using bcrypt algorithm
            hashed = bcrypt.hashpw(
                data['password'].encode('utf-8'), bcrypt.gensalt())

            # Generate token
            email_token = random_string_generator()

            # create user
            user = User.objects.create(
                user_name=data['user_name'].strip(),
                password=hashed,
                email_verification_token=email_token,
                user_type='customer',
            )

            # create customer
            customer = Customer.objects.create(
                user=user,
                first_name=data['first_name'],
                last_name=data['last_name'],
                email=data['email']
            )

            # saue user in database
            user.save()

            # save customer in database
            customer.save()

            email_verification_url = config("VERIFY_EMAIL_URL")
            message = "Registration was successful"
            customer_message_details = {
                'subject': 'Bouncer email verification',
                'text_content': "You are welcome on board.",
                'to': [data["email"]],
                'from_email': config("EMAIL_SENDER"),
                'html_content': 'Welcome on board, complete your registration by clicking the link below',
                'link_message': f'Welcome on board </br> Click on this <a href="{email_verification_url}/?token={email_token}">Link</a> to verify'

            }

            # send mail to the user
            send = send_email(customer_message_details)
            if send:
                return Response({'message': message, 'user_message': customer_message(data)}, status=status.HTTP_201_CREATED)
            else:
                return Response(dict(message='Network Error: Could not send email at the moment You are registered'), status=status.HTTP_503_SERVICE_UNAVAILABLE)
