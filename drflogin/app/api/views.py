from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth.models import User
from app.api.serializer import LoginSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate,login,logout


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
                token=Token.objects.get_or_create(user=user)

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
        
        

        