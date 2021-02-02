from django.urls import path
from rango import views
app_name = 'rango'

urlpatterns = [
path('', views.index, name='index'),
path('about/', views.about, name='about'),
path('university/', views.uni, name='university'),
path('college/', views.college, name='college'),
path('apprenticeship/', views.apprenticeship, name='apprenticeship'),
path('uniCourse/<slug:uni_course_slug>/', views.uni_course, name='uni_course'),
path('collegeCourse/<slug:college_course_slug>/', views.college_course, name='college_course'),
path('apprenticeshipCourse/<slug:apprenticeship_course_slug>/', views.apprenticeship_course, name='apprenticeship_course'),
path('searchResults/', views.SearchResults, name='search_results'),
]

