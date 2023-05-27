from django.db import models

# Create your models here.

class Todo(models.Model):
    title=models.CharField(max_length=25)
    img=models.ImageField(upload_to='app/static/img')
