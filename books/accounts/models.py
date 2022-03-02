import imp
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    firstname = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=11, null=True)
    address = models.CharField(max_length=200, null=True)