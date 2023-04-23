from django.http import HttpResponse
from django.shortcuts import render
from app.models import *

def index(request):
    cat1=Category.objects.all()


    



    return render(request,'index.html',{"category":cat1})

