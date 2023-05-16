from rest_framework import serializers
from django.contrib.auth.models import User 
from app.models import Todo
# Toxunursuz donur

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Todo 
        fields = "__all__"