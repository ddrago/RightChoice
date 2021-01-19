from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
import uuid
from django.conf import settings

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='Joe Bloggs')
    email = models.CharField(max_length=128, default='joebloggs@gmail.com')
    profilePicture = models.ImageField(upload_to='profile_images', blank=True, editable=True)
    savedPages = models.CharField(max_length=100, default='Page')

    def __str__(self):
        return self.user.username

class University(models.Model):
    name = models.CharField(primary_key=True, unique=True, max_length=128)
    location = models.CharField(max_length=128, default='Place')
    details = models.CharField(max_length=248, default='Description')
    universityImage = models.ImageField(upload_to= 'uni_images/',default='uni.jpg')
    slug = models.SlugField(unique=True, default=uuid.uuid1)
    linkToUniWebsite = models.URLField(default='Link')

    class Meta:
        verbose_name_plural = 'Universities'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(University, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class College(models.Model):
    name = models.CharField(primary_key=True, unique=True, max_length=128)
    location = models.CharField(max_length=128, default='Place')
    details = models.CharField(max_length=248, default='Description')
    collegeImage = models.ImageField(upload_to= 'college_images/',default='college.jpg')
    slug = models.SlugField(unique=True, default=uuid.uuid1)
    linkToCollegeWebsite = models.URLField(default='Link')

    class Meta:
        verbose_name_plural = 'Colleges'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(College, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(primary_key=True, unique=True, max_length=128)
    location = models.CharField(max_length=128, default='Place')
    details = models.CharField(max_length=248, default='Description')
    companyImage = models.ImageField(upload_to= 'college_images/',default='college.jpg')
    slug = models.SlugField(unique=True, default=uuid.uuid1)
    linkToCompanyWebsite = models.URLField(default='Link')

    class Meta:
        verbose_name_plural = 'Companies'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Company, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Apprenticeship(models.Model):
    name = models.CharField(primary_key=True, unique=True, max_length=128)
    location = models.CharField(max_length=128, default='Place')
    details = models.CharField(max_length=248, default='Description')
    companyImage = models.ImageField(upload_to= 'company_images/',default='company.jpg')
    slug = models.SlugField(unique=True, default=uuid.uuid1)
    linkToCompanyWebsite = models.URLField(default='Link')

    class Meta:
        verbose_name_plural = 'Apprenticeships'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Apprenticeship, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Career(models.Model):
    careerName = models.CharField(primary_key=True, unique=True, max_length=128)
    areaStudy = models.CharField(max_length=128, default='Area of study')

    class Meta:
        verbose_name_plural = 'Career'

    def __str__(self):
        return self.careerName

class SchoolSubjects(models.Model):
    name = models.CharField(max_length=128)
    level = models.CharField(max_length=128)
    career_name = models.ManyToManyField(Career, related_name="sub_career")
    subjectArea = models.CharField(max_length=128, default='Subject area')
    class Meta:
        unique_together = (("name","level"),)
        verbose_name_plural = 'SchoolSubjects'

    def __str__(self):
        return self.name

class Course_Uni(models.Model):
    courseID = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length = 128, default='Course')
    universityName = models.ForeignKey(University, on_delete=models.CASCADE)
    careerName = models.ManyToManyField(Career, related_name="uni_course")
    subReqName = models.ManyToManyField(SchoolSubjects, related_name="uni_course")
    gradesReq = models.CharField(max_length=100, default='Grades')
    subjectSuggestions = models.CharField(max_length = 248, default='Courses')
    slug = models.SlugField(unique=True, default=uuid.uuid1)

    class Meta:
        verbose_name_plural = 'Course_Uni'

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.courseID) + self.universityName.name)
        super(Course_Uni, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.courseID)

class Course_College(models.Model):
    courseID = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length = 128, default='Course')
    collegeName = models.ForeignKey(College, on_delete=models.CASCADE)
    careerName = models.ManyToManyField(Career, related_name="college_course")
    subReqName = models.ManyToManyField(SchoolSubjects, related_name="college_course")
    gradesReq = models.CharField(max_length=100, default='Grades')
    subjectSuggestions = models.CharField(max_length = 248, default='Courses')
    slug = models.SlugField(unique=True, default=uuid.uuid1)

    class Meta:
        verbose_name_plural = 'Course_College'

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.courseID) + self.collegeName.name)
        super(Course_College, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.courseID)

class Course_Apprenticeship(models.Model):
    courseID = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length = 128, default='Course')
    companyName = models.ForeignKey(Company, on_delete=models.CASCADE)
    careerName = models.ManyToManyField(Career, related_name="apprenticeship_course")
    #subReqName = models.ManyToManyField(SchoolSubjects, related_name="apprenticeship_course") most apprentieships dont have this
    gradesReq = models.CharField(max_length=100, default='Grades')
    subjectSuggestions = models.CharField(max_length = 248, default='Courses')
    slug = models.SlugField(unique=True, default=uuid.uuid1)

    class Meta:
        verbose_name_plural = 'Course_Apprenticeship'


    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.courseID) + self.companyName.name)
        super(Course_Apprenticeship, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.courseID)
