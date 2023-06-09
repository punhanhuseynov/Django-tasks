# Generated by Django 4.2 on 2023-05-03 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_questions_variant1_alter_questions_variant2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questioncategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='questions',
            name='questcategory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.questioncategory'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='result',
            name='questcategory',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='app.questioncategory'),
            preserve_default=False,
        ),
    ]
