from rest_framework import serializers
from app.models import *

class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model=Books
        fields="__all__"