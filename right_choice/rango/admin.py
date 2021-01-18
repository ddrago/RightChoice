from django.contrib import admin
from rango.models import UserProfile, University, College, Apprenticeship, Career, SchoolSubjects, Course_Uni, Course_College, Course_Apprenticeship

admin.site.register(UserProfile)
admin.site.register(University)
admin.site.register(College)
admin.site.register(Apprenticeship)
admin.site.register(Career)
admin.site.register(SchoolSubjects)
admin.site.register(Course_Uni)
admin.site.register(Course_College)
admin.site.register(Course_Apprenticeship)

# Register your models here.
