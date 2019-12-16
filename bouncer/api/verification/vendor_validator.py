import re
from rest_framework.response import Response
from rest_framework import status
from ..utils.helper import *
from ..verification.customer_validator import email_already_exist, is_valid_username


# This function Check missing fields and return  an object of missing field if any and True there is no missing field
def check_missing_fields(data):
    keys = ['user_name', 'password', 'shop_name', 'email']
    missing_fields = {}
    for key in keys:
        value = data.get(key)
        if not check_empty_value(value):
            missing_fields[key] = key +" must not be empty"
    if missing_fields == {}:
        return True
    else:
        return missing_fields
    
# This function check for existing shop name
def is_valid_shopname(data, model):
    try:
        is_valid_shopname = model.objects.get(shop_name=data.get('shop_name'))
        if is_valid_shopname:
            return False
    except:
        return True
    
def validate(data, user, vendor):
    
    missing_field = check_missing_fields(data)
    
    if missing_field != True:
        
        return Response({"message":missing_field},status=status.HTTP_400_BAD_REQUEST)
    
    if is_valid_username(data, user) != True or validate_len(data.get('user_name'), 5):
        
        return Response({"message":"Invalid Username!!!  Username already exist or less than five characters"},status=status.HTTP_400_BAD_REQUEST)
    
    if regex_validator(data.get('user_name'), username_regex)==False:
                
        return Response({"message":"Invalid Username!!!  Username must not contain white space(s) or start with numbers or special characters"},status=status.HTTP_400_BAD_REQUEST)
            
    if regex_validator(data.get('email'), email_regex) == False or email_already_exist(data, vendor) != True:
        return Response({"message":"Email is invalid or already exist"},status=status.HTTP_400_BAD_REQUEST)
                
    if validate_len(data.get('password'), 6):
        return Response({"message":"Invalid Password! Password must contain 6 or more characters"},status=status.HTTP_400_BAD_REQUEST)
                    
    if is_valid_shopname(data, vendor) != True or validate_len(data.get('shop_name'), 2):
        return Response({"message":"Shop name already exist or less than two characters"}, status=status.HTTP_400_BAD_REQUEST)
        
    return True
                        