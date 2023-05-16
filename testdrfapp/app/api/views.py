from app.api.serializers import Todoserializers
from app.models import Todo

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['GET','POST'])
def create_todo_list_view(request):
    todo=Todo.objects.all()
    serializers=Todoserializers(todo,many=True)
    if request.method=='POST':
        data=Todoserializers(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data,status=status.HTTP_201_CREATED)
            
    return Response(serializers.data)

@api_view(['GET','PUT',"DELETE"])
def read_todo_view(request,id):
    todo=Todo.objects.filter(id=id).first()
    serilizer=Todoserializers(todo)

    if request.method=='PUT':
        if todo:
            newserializer=Todoserializers(todo,data=request.data)
            if newserializer.is_valid():
                newserializer.save()
                return Response(newserializer.data,status=status.HTTP_200_OK)
    if request.method=='DELETE':
        if todo:
            
            todo.delete()
            return Response(status=status.HTTP_200_OK)

    return Response(serilizer.data,status=status.HTTP_200_OK)

   

