# Generated by Django 4.2 on 2023-04-21 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Categoryphone',
        ),
        migrations.CreateModel(
            name='Categorybrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.categoryphone')),
            ],
        ),
    ]
