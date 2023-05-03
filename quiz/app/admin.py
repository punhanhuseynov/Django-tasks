from django.contrib import admin

# Register your models here.


from app.models import Questions,Result,Questioncategory

admin.site.register(Questioncategory)
admin.site.register(Questions)
admin.site.register(Result)
