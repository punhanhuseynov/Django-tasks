# Generated by Django 4.2 on 2023-04-22 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_category_cat_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child', to='app.category'),
        ),
    ]
