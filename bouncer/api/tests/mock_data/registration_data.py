
def customer_registration_data():
    return {
        "last_name": "test",
        "first_name": "test_name",
        "email": "test@gmail.com",
        "user_name": "testuser",
        "password": "testpassword",
        "user_type": "customer",
        "email_verification_token": "hjfdsjkfl3"
    }

def vendor_registration_data():
    return {
        "shop_name": "best4less",
        "email": "test@gmail.com",
        "user_name": "testuser",
        "password": "testpassword",
        "user_type": "vendor",
        "email_verification_token": "hjfdsjkfl3"
    }
    
def user_registration_data():
    return {
    "id":8,
    "user_name": "ola",
    "password": "hello",
    "user_type": "customer",
    "email_verified":False,
    "email_verification_token":"123456"
}
    
def forgot_password_customer_registration_data():
    return {
    "last_name": "Doe",
    "first_name": "John",
    "email": "johnDoe@gmail.com",
    "user_name": "customer_jd",
    "password": "testpassword",
    "user_type": "customer",
    "token": "hjfdsjkfl3"
}

    
def forgot_password_vendor_registration_data():
    return {
    "shop_name": "AnotherBest4less",
    "email": "anothertest@gmail.com",
    "user_name": "vendor_jd",
    "password": "testpassword",
    "user_type": "vendor",
    "token": "hjfdsjkfl3"
}


