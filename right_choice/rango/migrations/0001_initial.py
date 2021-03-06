# Generated by Django 2.1.5 on 2021-01-13 15:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Apprenticeship',
            fields=[
                ('name', models.CharField(max_length=128, primary_key=True, serialize=False, unique=True)),
                ('location', models.CharField(default='Place', max_length=128)),
                ('details', models.CharField(default='Description', max_length=248)),
                ('companyImage', models.ImageField(default='college.jpg', upload_to='college_images/')),
                ('slug', models.SlugField(default=uuid.uuid1, unique=True)),
                ('linkToCompanyWebsite', models.URLField(default='Link')),
            ],
        ),
        migrations.CreateModel(
            name='Career',
            fields=[
                ('careerName', models.CharField(max_length=128, primary_key=True, serialize=False, unique=True)),
                ('areaStudy', models.CharField(default='Area of study', max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('name', models.CharField(max_length=128, primary_key=True, serialize=False, unique=True)),
                ('location', models.CharField(default='Place', max_length=128)),
                ('details', models.CharField(default='Description', max_length=248)),
                ('collegeImage', models.ImageField(default='college.jpg', upload_to='college_images/')),
                ('slug', models.SlugField(default=uuid.uuid1, unique=True)),
                ('linkToCollegeWebsite', models.URLField(default='Link')),
            ],
        ),
        migrations.CreateModel(
            name='Course_Apprenticeship',
            fields=[
                ('courseID', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(default='Course', max_length=128)),
                ('gradesReq', models.CharField(default='Grades', max_length=100)),
                ('subjectSuggestions', models.CharField(default='Courses', max_length=248)),
                ('slug', models.SlugField(default=uuid.uuid1, unique=True)),
                ('careerName', models.ManyToManyField(related_name='apprenticeship_course', to='rango.Career')),
                ('companyName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rango.College')),
            ],
        ),
        migrations.CreateModel(
            name='Course_College',
            fields=[
                ('courseID', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(default='Course', max_length=128)),
                ('gradesReq', models.CharField(default='Grades', max_length=100)),
                ('subjectSuggestions', models.CharField(default='Courses', max_length=248)),
                ('slug', models.SlugField(default=uuid.uuid1, unique=True)),
                ('careerName', models.ManyToManyField(related_name='college_course', to='rango.Career')),
                ('collegeName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rango.College')),
            ],
        ),
        migrations.CreateModel(
            name='Course_Uni',
            fields=[
                ('courseID', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(default='Course', max_length=128)),
                ('gradesReq', models.CharField(default='Grades', max_length=100)),
                ('subjectSuggestions', models.CharField(default='Courses', max_length=248)),
                ('slug', models.SlugField(default=uuid.uuid1, unique=True)),
                ('careerName', models.ManyToManyField(related_name='uni_course', to='rango.Career')),
            ],
        ),
        migrations.CreateModel(
            name='SchoolSubjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('level', models.CharField(max_length=128)),
                ('subjectArea', models.CharField(default='Subject area', max_length=128)),
                ('career_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rango.Career')),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('name', models.CharField(max_length=128, primary_key=True, serialize=False, unique=True)),
                ('location', models.CharField(default='Place', max_length=128)),
                ('genre', models.CharField(default='Genre', max_length=128)),
                ('details', models.CharField(default='Description', max_length=248)),
                ('universityImage', models.ImageField(default='uni.jpg', upload_to='uni_images/')),
                ('slug', models.SlugField(default=uuid.uuid1, unique=True)),
                ('linkToUniWebsite', models.URLField(default='Link')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Joe Bloggs', max_length=50)),
                ('email', models.CharField(default='joebloggs@gmail.com', max_length=128)),
                ('profilePicture', models.ImageField(blank=True, upload_to='profile_images')),
                ('savedPages', models.CharField(default='Page', max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='course_uni',
            name='subReqName',
            field=models.ManyToManyField(related_name='uni_course', to='rango.SchoolSubjects'),
        ),
        migrations.AddField(
            model_name='course_uni',
            name='universityName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rango.University'),
        ),
        migrations.AddField(
            model_name='course_college',
            name='subReqName',
            field=models.ManyToManyField(related_name='college_course', to='rango.SchoolSubjects'),
        ),
        migrations.AddField(
            model_name='course_apprenticeship',
            name='subReqName',
            field=models.ManyToManyField(related_name='apprenticeship_course', to='rango.SchoolSubjects'),
        ),
        migrations.AlterUniqueTogether(
            name='schoolsubjects',
            unique_together={('name', 'level')},
        ),
    ]
