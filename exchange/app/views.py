from django.shortcuts import render

# Create your views here.

#Route for main page
def index(request):
    
    return render(request,'index.html')
