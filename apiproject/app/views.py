from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
# Create your views here.
from app.models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework_simplejwt.views import TokenObtainPairView


def index(request):
    
    return render(request,'index.html')
def testapi(request):
    todo=Todo.objects.all()
    seri=TodoSerializer(todo,many=True)
    
    return render(request,'test.html',{"data":seri.data})

# class MyTokenObtainPaiView(TokenObtainPairView):
#     serializer_class=MyTokenObtainPairSrializer