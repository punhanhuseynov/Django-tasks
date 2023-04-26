from django.db import models


# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=20)
    
    price=models.CharField(max_length=20)
    
    def __str__(self):
        return self.name


class Cart(models.Model):
  
    user_id=models.IntegerField(default=1)

    product_id=models.ForeignKey('Product',on_delete=models.CASCADE,related_name='carts')
    
  
