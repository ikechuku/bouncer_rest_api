from django.core.mail import send_mail

from rest_framework.views import APIView

import bcrypt
from decouple import config

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
            
            # saue user in database
            user.save()

            # save customer in database
            customer.save()

            # send mail to the user
            return send_email(data, token)
