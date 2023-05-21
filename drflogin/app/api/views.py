from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth.models import User
from app.api.serializer import LoginSerializer,RegisterSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate,login,logout

from django.core.mail import send_mail

class UserLoginView(APIView):
    
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
                token=Token.objects.get(user=user)

                login(request,user)

                return Response(
                {
                "message":'welcome'
                }

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

        