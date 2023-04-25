from django.db import models
from django.contrib import admin
from mptt.models import MPTTModel,TreeForeignKey
from mptt.admin import MPTTModelAdmin

class Category(MPTTModel):
    
    name=models.CharField(max_length=20)
    parent=TreeForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='children')
    

    class MPTTMeta:
        order_insertion_by=['name']

    def __str__(self):
        return self.name



admin.site.register(Category,MPTTModelAdmin)
