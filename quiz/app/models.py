from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Questioncategory(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.name
    
class Questions(models.Model):
    questcategory=models.ForeignKey(Questioncategory,on_delete=models.CASCADE)
    question=models.CharField(max_length=30)
    answer=models.CharField(max_length=30)
    variant1=models.CharField(max_length=30)
    variant2=models.CharField(max_length=30)
    variant3=models.CharField(max_length=30)
    variant4=models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.question

class Result(models.Model):
    questcategory=models.ForeignKey(Questioncategory,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    trueanswers=models.CharField(max_length=50)
    falseanswers=models.CharField(max_length=50)


