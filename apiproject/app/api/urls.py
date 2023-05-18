from django.urls import path, include
from app.api.views import *

urlpatterns = [
    path('books/',list_all_books),
    path('books/<id>',book_detail),
    path('login/',login_view)

]