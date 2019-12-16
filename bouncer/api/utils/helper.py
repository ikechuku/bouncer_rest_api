import random
import string
import re

#This function generates 8 random alphanumeric characters
def random_string_generator(size=8, chars=string.ascii_lowercase + string.digits+ string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))    

# This function validate len of value if is greather than num
def validate_len(value, num):
    return True if len(value) < num else False

# This regex checks if email is valid
email_regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

# This regex checks if a word start with alphabet, must not contain space, and other characters except underscore and hyphen
username_regex = '^([a-zA-Z])[a-zA-Z_-]*[\w_-]*[\S]$|^([a-zA-Z])[0-9_-]*[\S]$|^[a-zA-Z]*[\S]$'

def regex_validator(value, regex):
    if not value:
        return False
    else:
        return bool(re.search(regex, value))

# This funciton checks if the value is empty 
def check_empty_value(value):
    return bool(value)
