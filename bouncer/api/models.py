from django.db import models

class CustomUser(models.Model):
    user_name = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=250, null=False)
    token = models.CharField( max_length=20)
    is_vendor = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    email = models.EmailField(max_length=254, unique=True,default="abc@gmail.com")
    email_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user_name