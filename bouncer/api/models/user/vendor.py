from django.db import models
from .users import User

class Customers(models.Model):
    shop_name = models.CharField(max_length=250, null=False, unique=True)
    account_verified = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.shop_name