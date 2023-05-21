from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","email",'password',"first_name","last_name"]

    def create(self,validated_data):
        password=validated_data.pop('password')
        user=User.objects.create(password=make_password(password),**validated_data)
        return user