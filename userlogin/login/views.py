from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
def index(request):
    
    return render(request,'index.html')

def login_user(request):
    if request.method=='POST':
        name=request.POST['username']
        password=request.POST['password']
        
        user=authenticate(request,username=name,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return HttpResponse('wrong')

    return render(request,'login.html')

def logout_user(request):
    logout(request)
    return redirect('/login')


def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password_again=request.POST['password_again']
        if password==password_again:
            data=User.objects.create_user(username=username,email=email,password=password)
            
            return redirect('/login')
        else:
            return 'wrong password'
    return render(request,'register.html')