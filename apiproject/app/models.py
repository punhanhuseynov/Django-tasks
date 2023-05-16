from django.db import models
from rest_framework import serializers,generics
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# Create your models here.




class Todo(models.Model):
    name=models.CharField(max_length=30)

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Todo
        fields=['id','name']

# class MyTokenObtainPairSrializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token=super().get_token(user)
    
#         return token