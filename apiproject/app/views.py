from django.shortcuts import render

# Create your views here.
from app.models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework_simplejwt.views import TokenObtainPairView


def index(request):
    
    return render(request,'index.html')

class MyTokenObtainPaiView(TokenObtainPairView):
    serializer_class=MyTokenObtainPairSrializer