from django.db import models
from django.contrib import admin

class Category(models.Model):
   
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Phone(models.Model):
    name=models.CharField(max_length=20)
    category=models.ForeignKey('Category',on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Models(models.Model):
    name=models.CharField(max_length=20)
    category=models.ForeignKey('Phone',on_delete=models.CASCADE)

    def __str__(self):
        return self.name




admin.site.register(Category)
admin.site.register(Phone)
admin.site.register(Models)