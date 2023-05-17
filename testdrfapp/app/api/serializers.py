from rest_framework import serializers
from app.models import Todo,Writer

# class Todoserializers(serializers.Serializer):
#     id=serializers.IntegerField(read_only=True)
#     name=serializers.CharField()
    
#     def create(self,validated_data):
#         return Todo.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name=validated_data.get('name',instance.name)
#         instance.save()
#         return instance

class Todoserializers(serializers.ModelSerializer):
    class Meta:
        model=Todo
        fields="__all__"

class Writerserializer(serializers.ModelSerializer):
    
    writer=Todoserializers(many=True,read_only=True)

    class Meta:
        model=Writer
        fields="__all__"
    