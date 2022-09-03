from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Authentication(AbstractUser):
    username=models.CharField(max_length=255,primary_key=True,unique=True)
    Contact_number=models.CharField(max_length=10)
    Gender=models.CharField(max_length=1)
    Age=models.CharField(max_length=3)
    is_medical = models.BooleanField(default = False)
    is_user = models.BooleanField(default=False)
    is_hospital = models.BooleanField(default=False)

    def __str__(self):
        return str(self.username)

"""class Contact_Messages(models.Model):
    username=models.CharField(max_length=255,primary_key=True)

    user_firstname = models.CharField(max_length = 255)

    user_lastname=models.CharField(max_length=255)

    user_mobilenumber=models.CharField(max_length=10)

    message=models.TextField()"""