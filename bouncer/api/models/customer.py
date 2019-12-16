from django.db import models
from .user import User

<<<<<<< HEAD:bouncer/api/models/customer.py
class Customer(models.Model):
=======
class Vendor(models.Model):
>>>>>>> rebase:bouncer/api/models/user/customers.py
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, unique=True, null=False)

    def __str__(self):
        return self.first_name
        