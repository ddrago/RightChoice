# Generated by Django 3.1.3 on 2021-01-19 14:19

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0003_remove_course_apprenticeship_subreqname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('name', models.CharField(max_length=128, primary_key=True, serialize=False, unique=True)),
                ('location', models.CharField(default='Place', max_length=128)),
                ('details', models.CharField(default='Description', max_length=248)),
                ('companyImage', models.ImageField(default='college.jpg', upload_to='college_images/')),
                ('slug', models.SlugField(default=uuid.uuid1, unique=True)),
                ('linkToCompanyWebsite', models.URLField(default='Link')),
            ],
            options={
                'verbose_name_plural': 'Colleges',
            },
        ),
        migrations.AlterField(
            model_name='apprenticeship',
            name='companyImage',
            field=models.ImageField(default='company.jpg', upload_to='company_images/'),
        ),
        migrations.AlterField(
            model_name='course_apprenticeship',
            name='companyName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rango.company'),
        ),
    ]