# Generated by Django 4.2 on 2023-04-26 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='cartname',
            field=models.CharField(default='kart', max_length=20),
        ),
    ]
