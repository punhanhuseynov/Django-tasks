from django.shortcuts import render,HttpResponse,redirect

# Create your views here.



def index(request):
    result=''
    number= ''
    if request.method=='POST':
        number=request.POST['number']
        numeral=request.POST['numeral']
        if numeral=='2':
            
            result=bin(int(number))[2:]
            
        
        elif numeral=='8':
            
            result=oct(int(number))[2:]
            
        

            
        
        elif numeral=='16':
            result=hex(int(number))[2:]
        
                
    
    return render(request,'index.html',{'result':result,'number':number})

def add(request):
    pass

        
        
    