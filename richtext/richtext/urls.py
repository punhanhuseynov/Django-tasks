from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib import admin
from django.urls import path, include
from app.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
  
   path('ckeditor/', include('ckeditor_uploader.urls')),


    path('', index),
]
