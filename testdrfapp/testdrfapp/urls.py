"""
URL configuration for testdrfapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.api.views import ListAllTodosView,TododetailView,Listallwriterview


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/writers',Listallwriterview.as_view()),
    path('api/todo',ListAllTodosView.as_view()),
    path('api/todo/<id>',TododetailView.as_view())

    
]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/todo',create_todo_list_view),
#     path('api/todo/<id>',read_todo_view)

    
# ]

