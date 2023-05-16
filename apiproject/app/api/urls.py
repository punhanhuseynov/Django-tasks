from django.urls import path 

from app.api.views import *


urlpatterns = [
    path('login/',LoginAPIView.as_view(), name="login"),
    path('todos/', TodoListAPIView.as_view(), name='todo-lists'),
]