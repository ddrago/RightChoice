from django.urls import path
from rango import views
app_name = 'rango'

urlpatterns = [
path('', views.index, name='index'),
path('about/', views.about, name='about'),
path('universities/', views.universities, name='universities'),
path('university/<slug:university_slug>/', views.uni, name='university'),
path('university/searchResults/<slug:university_slug>/', views.search_results_uni, name='search_results_uni'),
path('colleges/', views.colleges, name='colleges'),
path('apprenticeship/', views.apprenticeship, name='apprenticeship'),
path('uniCourse/<slug:uni_course_slug>/', views.uni_course, name='uni_course'),
path('collegeCourse/<slug:college_course_slug>/', views.college_course, name='college_course'),
path('apprenticeshipCourse/<slug:apprenticeship_course_slug>/', views.apprenticeship_course, name='apprenticeship_course'),
path('searchResults/', views.SearchResults, name='search_results'),
]

