from rest_framework import serializers
from app.models import Book

class LoginSerializer(serializers.ModelSerializer):
    username=serializers.CharField()
    password=serializers.CharField()

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields="__all__"