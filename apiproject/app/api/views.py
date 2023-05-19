from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework import status,permissions
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication,BasicAuthentication
from .serializers import BookSerializer,LoginSerializer
from app.models import Book
from django.contrib.auth import authenticate,login,logout
from rest_framework.authtoken.models import Token




@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def login_view(request):
    if request.method=='POST':
        serializer=LoginSerializer(data=request.data)
       
        if serializer.is_valid():
            username=serializer.validated_data.get('username')
            password=serializer.validated_data.get('password')
    
            user=authenticate(request=request,username=username,password=password)
            if user is not None:
                # login(request,user)
                token,created=Token.objects.get_or_create(user=user)
                print(token)
                return Response(
                    {
                        "message":token.key
                    }
                    ,status=status.HTTP_200_OK
                    )

    

@api_view(['GET','POST'])
@authentication_classes([TokenAuthentication,BasicAuthentication])
@permission_classes([permissions.IsAdminUser])
def list_all_books(request):
    try:token=Token.objects.get(user=request.user)
    except Token.DoesNotExist:
        return Response({
            "message":"This user not have token"
        },status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        book=Book.objects.all()
        serializer=BookSerializer(book,many=True)
        if token is not None:
            return Response({
                    "token":token.key,
                    "data":serializer.data
                    },status=status.HTTP_200_OK)

    if request.method=='POST':
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        
    
    

@api_view(['PUT','DELETE','GET'])
def book_detail(request,id):
    if request.method=='GET':
        book=Book.objects.get(id=id)
        serializer=BookSerializer(book)
        return Response(serializer.data,status=status.HTTP_200_OK)

