# Generated by Django 4.2 on 2023-05-04 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_wronganswers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Correctanswers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=80)),
                ('answer', models.CharField(max_length=80)),
                ('result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.result')),
            ],
        ),
    ]