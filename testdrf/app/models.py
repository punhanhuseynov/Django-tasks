from django.db import models

# Create your models here.

class Books(models.Model):
    author=models.CharField(max_length=25)
    title=models.CharField(max_length=40)
    desc=models.TextField()
    
