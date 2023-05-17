from app.api.serializers import Todoserializers,Writerserializer
from app.models import Todo,Writer

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics

class Listallwriterview(APIView):
    def get(self,request):
        writer=Writer.objects.all()
        serilizer=Writerserializer(writer,many=True)
        return Response(serilizer.data,status=status.HTTP_200_OK)

    def post(self,request):
        
        serializer=Writerserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

class ListAllTodosView(generics.ListCreateAPIView):
    queryset=Todo.objects.all()
    serializer_class=Todoserializers



# class ListAllTodosView(APIView):
#     def get(self,request):
#         todo=Todo.objects.all()
#         serializer=Todoserializers(todo,many=True)
        
#         return Response(serializer.data,status=status.HTTP_200_OK)
        
#     def post(self,request):
        
#         serializer=Todoserializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
        

class TododetailView(APIView):
    def get(self,request,id):
        todo=Todo.objects.filter(id=id).first()
        serializer=Todoserializers(todo)
        
        if todo:
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def put(self,request,id):
        todo=Todo.objects.filter(id=id).first()
        serializer=Todoserializers(todo,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
    def delete(self,request,id):
        todo=Todo.objects.filter(id=id)
        todo.delete()
        return Response({"message":'delete'},status=status.HTTP_200_OK)




# Function based Views

# @api_view(['GET','POST'])
# def create_todo_list_view(self,requestt):
#     todo=Todo.objects.all()
#     serializers=Todoserializers(todo,many=True)
#     if request.method=='POST':
#         data=Todoserializers(data=request.data)
#         if data.is_valid():
#             data.save()
#             return Response(data.data,status=status.HTTP_201_CREATED)
            
#     return Response(serializers.data)

# @api_view(['GET','PUT',"DELETE"])
# def read_todo_view(self,requestt,id):
#     todo=Todo.objects.filter(id=id).first()
#     serilizer=Todoserializers(todo)

#     if request.method=='PUT':
#         if todo:
#             newserializer=Todoserializers(todo,data=request.data)
#             if newserializer.is_valid():
#                 newserializer.save()
#                 return Response(newserializer.data,status=status.HTTP_200_OK)
#     if request.method=='DELETE':
#         if todo:
            
#             todo.delete()
#             return Response(status=status.HTTP_200_OK)

#     return Response(serilizer.data,status=status.HTTP_200_OK)


   

