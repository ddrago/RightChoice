# Generated by Django 2.1.5 on 2021-01-17 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20210117_1709'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course_apprenticeship',
            name='subReqName',
        ),
    ]