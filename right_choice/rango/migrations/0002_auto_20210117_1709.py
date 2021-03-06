# Generated by Django 2.1.5 on 2021-01-17 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='apprenticeship',
            options={'verbose_name_plural': 'Apprenticeships'},
        ),
        migrations.AlterModelOptions(
            name='career',
            options={'verbose_name_plural': 'Career'},
        ),
        migrations.AlterModelOptions(
            name='college',
            options={'verbose_name_plural': 'Colleges'},
        ),
        migrations.AlterModelOptions(
            name='course_apprenticeship',
            options={'verbose_name_plural': 'Course_Apprenticeship'},
        ),
        migrations.AlterModelOptions(
            name='course_college',
            options={'verbose_name_plural': 'Course_College'},
        ),
        migrations.AlterModelOptions(
            name='course_uni',
            options={'verbose_name_plural': 'Course_Uni'},
        ),
        migrations.AlterModelOptions(
            name='schoolsubjects',
            options={'verbose_name_plural': 'SchoolSubjects'},
        ),
        migrations.AlterModelOptions(
            name='university',
            options={'verbose_name_plural': 'Universities'},
        ),
        migrations.RemoveField(
            model_name='university',
            name='genre',
        ),
    ]
