from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth.models import User
from app.api.serializer import LoginSerializer,RegisterSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate,login,logout
from rest_framework_simplejwt.tokens import AccessToken,RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.core.mail import send_mail

class UserLoginView(APIView):
    permission_classes=[AllowAny]
    def get(self,request):
        return Response(
            {
                "message":'working'
            }
            
        )
    
    def post(self,request):
        posted_data=request.data
        serializer=LoginSerializer(data=posted_data)
        if serializer.is_valid():
            username=serializer.validated_data.get('username')
            password=serializer.validated_data.get('password')

            user=authenticate(request=request,username=username,password=password)
            if user is not None:
                token_access=AccessToken.for_user(user)
                token_refresh=RefreshToken.for_user(user)
                login(request,user)
                token={
                    "access":str(token_access),
                    "refresh":str(token_refresh)
                }
                return Response(
              
                {
                "message":'welcome',
                "token":token
                
                },status=status.HTTP_200_OK

                )
            else:
                 return Response(
            {
                "message":'wrongusername'
            }
            )
    
            
        else:
            return Response(
            {
                "message":'fill'
            }
            )

class UserRegistrationView(APIView):
    permission_classes=[AllowAny]
    def post(self,request):
        
        serializer=RegisterSerializer(data=request.data)
        if serializer.is_valid():

            serializer.save()
            user=User.objects.filter(username=serializer.validated_data.get('username')).first()
            token=Token.objects.get_or_create(user=user)
            data= f'http://localhost:8000/activate/user/{user.id}/'
            send_mail(
                "Hesab Doğrulaması ",
                'Hesabınızı təsdiq edin '+data,
                # 'husepunhan@gmail.com',
                # ['husepunhan@gmail.com'],
                fail_silently=False
            )
            return Response({'message':"created"})
        
        return Response(serializer.errors)

class TestView(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAdminUser]
    def get(self,request):
        return Response(status=status.HTTP_200_OK)

        