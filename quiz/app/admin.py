from django.contrib import admin

# Register your models here.


from app.models import *

admin.site.register(Questioncategory)
admin.site.register(Questions)
admin.site.register(Result)
admin.site.register(Wronganswers)
admin.site.register(Correctanswers)
