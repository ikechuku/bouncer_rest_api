import random
import string
import re
from rest_framework import status
from django.core.mail import send_mail
from decouple import config
from rest_framework.response import Response


#This function generates 8 random alphanumeric characters
def random_string_generator(size=8, chars=string.ascii_lowercase + string.digits+ string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))    

# This function validate len of value if is greather than num
def validate_len(value, num):
    return True if len(value) < num else False

# This regex checks if email is valid
email_regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

# This regex checks if a word starts with alphabet, must not contain space, and other characters except underscore and hyphen
username_regex = '^([a-zA-Z])[a-zA-Z_-]*[\w_-]*[\S]$|^([a-zA-Z])[0-9_-]*[\S]$|^[a-zA-Z]*[\S]$'

def regex_validator(value, regex):
    if not value:
        return False
    else:
        return bool(re.search(regex, value))

# This funciton checks if the value is empty 
def check_empty_value(value):
    return bool(value)

def customer_message(data):
    return {
    "first_name":data['first_name'],
    "last_name":data['last_name'],
    "user_name":data['user_name'].strip(),
    "email":data['email'],
}

def send_email(data, token):
    message = "Registration was successful"
    subject = 'Bouncer email verification'
    text_content= "You are welcome on board."
    to = [data["email"]]
    from_email = config("EMAIL_SENDER")
    email_verification_url=config("VERIFY_EMAIL_URL")
    html_content ='Welcome on board, complete your registration by clicking the link below'
    link_message = f'Welcome on board </br> Click on this <a href="{email_verification_url}/?token={token}">Link</a> to verify'
    try:
        send_mail(subject, html_content,from_email,to, fail_silently=False,  html_message=link_message)
        return Response(dict(message=message,customer=customer_message(data)),status=status.HTTP_201_CREATED)
    except:
        return Response(dict(message='Network Error: Could not send email at the moment You are registered'))
