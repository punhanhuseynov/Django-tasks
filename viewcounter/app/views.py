from django.shortcuts import render,HttpResponse

# Create your views here.

from app.models import *
from datetime import datetime,timedelta
def index(request):
    data=Product.objects.all()
    
    return render(request,'index.html',{'data':data})
    

def product(request,id):
    data=Product.objects.filter(id=id).first()

    ip=request.META.get('REMOTE_ADDR')

    now=datetime.now().strftime("%Y:%m:%d:%H:%M:%S")

    productviewers=request.session.get('viewed',{})

    fakedate=datetime(2023,4,29)

    if id not in productviewers:
        productviewers[id]={"date":now,"ip":ip}
        
        
        print(productviewers)
        data.viewers+=1
        data.save()
        request.session['viewed']=productviewers
        
        
    else:
        if ip in  productviewers[id]['ip']:
            
            if datetime.strptime(now,"%Y:%m:%d:%H:%M:%S")>datetime.strptime(productviewers[id]['date'],"%Y:%m:%d:%H:%M:%S")+timedelta(days=1):
                data.viewers+=1
                data.save()
                productviewers[id]['date']=now
            
            # return HttpResponse(f"{productviewers[id]['date']}-{datetime.strptime(productviewers[id]['date'],'%Y:%m:%d:%H:%M:%S')+timedelta(days=1)}")
      
        else:
            data.viewers+=1
            data.save()
        
    return render(request,'product.html',{'data':data})
        
        


    

