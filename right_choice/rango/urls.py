from django.urls import path
from rango import views
app_name = 'rango'

urlpatterns = [
path('', views.index, name='index'),
path('about/', views.about, name='about'),
path('universities/', views.universities, name='universities'),
path('universities/searchResultsUniversities', views.SearchResultsUniversities, name='SearchResultsUniversities'),
path('universities/searchResultsColleges', views.SearchResultsColleges, name='SearchResultsColleges'),
path('university/<slug:university_slug>/', views.uni, name='university'),
path('university/searchResults/<slug:university_slug>/', views.search_results_uni, name='search_results_uni'),
path('colleges/', views.colleges, name='colleges'),
path('college/<slug:college_slug>/', views.college, name='college'),
path('college/searchResults/<slug:college_slug>/', views.search_results_college, name='search_results_college'),
path('apprenticeships/', views.apprenticeships, name='apprenticeships'),
path('apprenticeships/searchResults/', views.search_results_apprenticeships, name='search_results_apprenticeships'),
path('uniCourse/<slug:uni_course_slug>/', views.uni_course, name='uni_course'),
path('collegeCourse/<slug:college_course_slug>/', views.college_course, name='college_course'),
path('apprenticeshipCourse/<slug:apprenticeship_course_slug>/', views.apprenticeship_course, name='apprenticeship_course'),
path('searchResults/', views.SearchResults, name='search_results'),
path(r'^uniMenuResults/(?P<subject>\w+)$', views.uniMenuResults, name='uni_menu_search_results'),
]

