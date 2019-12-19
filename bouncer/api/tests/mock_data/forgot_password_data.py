from ...models.user import User
from ...models.vendor import Vendor
from ...models.customer import Customer

def customer_forgot_password_data():
    return {
        "user_name": "customerDoe"
    }


def vendor_forgot_password_data():
    return {
        "user_name": "vendorDoe"
    }


def create_customer():
    user = User.objects.create(user_name= "customerDoe", password="pass123", user_type="customer", email_verified=False)
    customer = Customer.objects.create(last_name= "Doe", email="customer@gmail.com", first_name="customer", user=user)
    # print(customer.email)
    return customer

def create_vendor():
    user = User.objects.create(user_name= "vendorDoe", password="pass123", user_type="vendor", email_verified=False)
    vendor = Vendor.objects.create(shop_name= "Doe", email="vendor@gmail.com", account_verified=False, user=user)
    return vendor