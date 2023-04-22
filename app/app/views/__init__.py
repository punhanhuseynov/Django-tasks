from django.http import HttpResponse
from django.shortcuts import render
from app.models import *

def index(request):
    cat=Category.objects.all()
    catPhone=Brand.objects.all()
    catModels=Models.objects.all()
    return render(request,'index.html',{"category":cat,'phone':catPhone,'models':catModels})

