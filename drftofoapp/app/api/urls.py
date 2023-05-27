from django.urls import path
from .views import *
urlpatterns = [
    path('todos/',AllTodoView),
    path('todo/<id>',TodoDetailView),
]
