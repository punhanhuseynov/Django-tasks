from django.db import models

# Create your models here.

class Writer(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name

class Todo(models.Model):
    name=models.CharField(max_length=25)
    write=models.ForeignKey(Writer,on_delete=models.CASCADE,related_name='writer')