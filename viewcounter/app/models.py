from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=20)
    description=models.TextField()
    price=models.CharField(max_length=20)
    viewers=models.IntegerField(default=0)
