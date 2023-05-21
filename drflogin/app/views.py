from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    
    return render(request,'index.html',{"user":request.user})

def index_register(request):
    
    return render(request,'register.html')

def activate(request,id):
    user=User.objects.filter(id=id).first()
    if user is not None:
        # return HttpResponse(user.is_active)
        if user.is_active==False:
            user.is_active=True
            user.save()
            return HttpResponse('hesab dogrulandi')
        else:
            return redirect('/')
    return HttpResponse('dogrulanmadi')

@login_required
def user_logout(request):
    logout(request)
    return redirect('/')


    
