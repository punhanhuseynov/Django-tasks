from django.shortcuts import render

# Create your views here.


def index(request):

    ip_address = request.META.get('HTTP_X_FORWARDED_FOR')
    if ip_address:

        ip_address = ip_address.split(',')[0].strip()
    else:

        ip_address = request.META.get('REMOTE_ADDR')
  
    return render(request,'index.html',{'ip':ip_address})
