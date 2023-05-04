from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
# Create your views here.

from app.models import *
def userlogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)

        if user is None:

            return redirect('/login')
            
        
        else:
            login(request,user)
            
            return redirect('/')
    return render(request,'login.html')


@login_required
def index(request):
    
    result=Result.objects.all()
    question= Questioncategory.objects.all()
    wrong=Wronganswers.objects.all()
    
    
    return render(request,'index.html',{"quest":question,"user":request.user,"result":result,"wrong":wrong})


@login_required
def test(request,id):
    
 

    testresult=Result.objects.filter(
        user=request.user,
        questcategory=Questioncategory.objects.filter(id=id).first()
                                     )
    
    question=Questions.objects.filter(questcategory=Questioncategory.objects.filter(id=id).first())
    if question :
        if testresult:
            return redirect('/')
        else:
            return render(request,'test.html',{"quest":question})
    
    else:
        return redirect('/')

@login_required
def add(request):
    if request.method == 'POST':
        data=json.loads(request.body)

        print(data)
        result=Result(
            questcategory=Questioncategory.objects.filter(id=data['category_id']).first(),
            user=request.user,
            trueanswers=data['true'],
            falseanswers=data['false']  
              )
        
        result.save()

        if data['result']:
            for w in data['result']:
                wrong=Wronganswers(question=w['question'],correct=w['correct'],answer=w['answer'],result=result,)
                wrong.save()


        return JsonResponse({"res":data})