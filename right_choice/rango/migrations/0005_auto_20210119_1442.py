# Generated by Django 3.1.3 on 2021-01-19 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0004_auto_20210119_1419'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name_plural': 'Companies'},
        ),
        migrations.RemoveField(
            model_name='schoolsubjects',
            name='career_name',
        ),
        migrations.AddField(
            model_name='schoolsubjects',
            name='career_name',
            field=models.ManyToManyField(related_name='sub_career', to='rango.Career'),
        ),
    ]
