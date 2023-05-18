from rest_framework.decorators import api_view,permission_classes
from rest_framework import status,permissions
from rest_framework.response import Response
from .serializers import BookSerializer,LoginSerializer
from app.models import Book
from django.contrib.auth import authenticate,login,logout


@api_view(['POST'])
def login_view(request):
    if request.method=='POST':
        serializer=LoginSerializer(data=request.data)
        if serializer.is_valid():
            username=serializer.validated_data.get('username')
            password=serializer.validated_data.get('password')

            user=authenticate(request=request,username=username,password=password)
            if user is not None:
                login(user)
                return Response({
                    "message":"login is true"
                },status=status.HTTP_200_OK)
        
    
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    

@api_view(['GET','POST'])
@permission_classes([permissions.IsAdminUser])
def list_all_books(request):
    book=Book.objects.all()
    serializer=BookSerializer(book,many=True)

    if request.method=='POST':
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        
    return Response(serializer.data,status=status.HTTP_200_OK)

    

@api_view(['PUT','DELETE','GET'])
def book_detail(request,id):
    if request.method=='GET':
        book=Book.objects.get(id=id)
        serializer=BookSerializer(book)
        return Response(serializer.data,status=status.HTTP_200_OK)

