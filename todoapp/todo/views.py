from django.shortcuts import render,redirect

# Create your views here.
from todo.models import *

def index(request):
    data=Todo.objects.all()
    
    return render(request,'index.html',{"data":data})

def read(request,id):
    todo=Todo.objects.filter(id=id).first()

    return render(request,'read.html',{"todo":todo})

def add_todo(request):
    if request.method=='POST':
        
        newtodo=Todo(title=request.POST['title'],fullpost=request.POST['text'])

        newtodo.save()
        return redirect('/')

    
    return redirect('/')


def delete_todo(request,id):
    data=Todo.objects.filter(id=id).first()
    data.delete()

    return redirect('/')

def update_todo(request,id):
    todo=Todo.objects.filter(id=id).first()

    if request.method=='POST':
        todo.title=request.POST['title']
        todo.fullpost=request.POST['text']
        todo.save()
        return redirect('/')
    return render(request,'update.html',{"todo":todo})