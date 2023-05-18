
from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)
from app.api import urls as api_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(api_urls))

]
