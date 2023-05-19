from django.db import models
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    name=models.CharField(max_length=25)
    writer=models.CharField(max_length=25)