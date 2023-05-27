from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import *

import os 

@api_view(["GET",'POST'])
def AllTodoView(request):
    todo=Todo.objects.all()
    serializer=TodoSerializers(todo,many=True)
    
    if request.method=='POST':
        seri=TodoSerializers(data=request.data)
        if seri.is_valid():
            seri.save()
        
        return Response(seri.data,status=status.HTTP_200_OK)

    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET','PUT','DELETE'])
def TodoDetailView(request,id):
    
    todo=Todo.objects.filter(id=id).first()
    serializer=TodoSerializers(todo)

    if request.method=='PUT':
        serializer=TodoSerializers(todo,data=request.data)
        
        if serializer.is_valid():
            os.remove(str(todo.img))
            serializer.save()
            return Response(serializer.data)
        
    if request.method=='DELETE':
        os.remove(str(todo.img))
        todo.delete()
        return Response({"message":'deleted'})
    return Response(serializer.data)
