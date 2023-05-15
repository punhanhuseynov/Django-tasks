
from django.contrib import admin
from django.urls import path

from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)

from app.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('api/token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('api/token/refresh/',TokenRefreshView.as_view(),name='token_refresh')
]
