from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Reviews(models.Model):
    username=models.CharField(max_length=25)
    content=RichTextField()

