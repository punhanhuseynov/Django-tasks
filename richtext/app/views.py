from django.shortcuts import render,redirect
from django.utils.html import mark_safe
from app.models import *
# Create your views here.
from app.forms import ReviewForm
def index(request):
    form=ReviewForm()
    data=Reviews.objects.all()
    
    if request.method=='POST':
        f=ReviewForm(request.POST)
        f.save()
        return redirect('/')
    return render(request,'index.html',{'form':form,"data":data})