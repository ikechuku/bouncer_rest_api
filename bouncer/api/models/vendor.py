from django.db import models
from .user import User


class Vendor(models.Model):
    shop_name = models.CharField(max_length=50, unique=True, null=False)
    email = models.EmailField(max_length=254, unique=True, null=False)
    account_verified = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.shop_name
    