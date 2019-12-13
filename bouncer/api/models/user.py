from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=250, null=False)
    token = models.CharField( max_length=20)
    user_type = models.CharField(max_length=30)
    email_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user_name
