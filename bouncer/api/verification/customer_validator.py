import re

from rest_framework.response import Response
from rest_framework import status

from ..utils.helper import  * 

def validate(data, user, customer):
    if missing_field(data) != True:
        return Response({"message":missing_field(data)},status=status.HTTP_400_BAD_REQUEST)
    else:
        if is_valid_username(data, user) != True or validate_len(data.get('user_name', ''), 5):
            return Response({"message":"Invalid Username!!!  Username already exist or less than five characters"},status=status.HTTP_400_BAD_REQUEST)
        else:
            if regex_validator(data.get('user_name', ''), username_regex)==False:
                return Response({"message":"Invalid Username!!!  Username must not contain white space(s) or startwith numbers or special characters"},status=status.HTTP_400_BAD_REQUEST)
            else:
                if regex_validator(data.get('email', ''), email_regex) == False or email_already_exist(data, customer) != True:
                    return Response({"message":"Email is invalid or already exist"},status=status.HTTP_400_BAD_REQUEST)
                else:
                    if validate_len(data.get('password', ''), 6):
                        return Response({"message":"Invalid Password! Password must contain 6 or more characters"},status=status.HTTP_400_BAD_REQUEST)
                    else:
                        return True


# This function Check missing fields and return  an object of missing field if any and True there is no missing field
def missing_field(data):
    keys = ['user_name', 'password', 'first_name', 'last_name', 'email']
    missing_fields = {}
    for key in keys:
        value = data.get(key, '')
        if not check_empty_value(value):
            missing_fields[key] = key +" must not be empty"
    if missing_fields == {}:
        return True
    else:
        return missing_fields

# This function check if email already exist 
def email_already_exist(data, model):
    try:
        is_email_already_exist = model.objects.get(email=data.get('email', ''))
        if is_email_already_exist:
            return False
    except:
        return True

# This function check if username already exist
def is_valid_username(data, model):
    try:
        is_valid_username = model.objects.get(user_name=data.get('user_name', ''))
        if is_valid_username:
            return False
    except:
        return True
   