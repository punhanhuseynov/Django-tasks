# Generated by Django 4.2 on 2023-04-26 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_product_cart_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='cartname',
        ),
    ]
