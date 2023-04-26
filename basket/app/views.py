from django.shortcuts import render,redirect

# Create your views here.

from app.models import *

userid=1


def index(request):
    product=Product.objects.all()
    cart=Cart.objects.filter(user_id=userid)
   
    return render(request,'index.html',{'product':product,'cart':cart})




def addcart(request,id):

    product=Product.objects.filter(id=id).first()
    cart=Cart(user_id=userid,product_id=product)
    cart.save()
    
    return redirect('/')

def deletecart(request,id):

    
    cart=Cart.objects.filter(id=id).first()
    cart.delete()
 
    
    return redirect('/')

