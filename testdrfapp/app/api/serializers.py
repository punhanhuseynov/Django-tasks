from rest_framework import serializers
from app.models import Todo

class Todoserializers(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    
    def create(self,validated_data):
        return Todo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.save()
        return instance
    