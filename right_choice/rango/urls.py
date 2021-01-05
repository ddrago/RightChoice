from django.urls import path
from rango import views
app_name = 'rango'
urlpatterns = [
path('', views.index, name='index'),
path('about/', views.about, name='about'),
path('university/', views.uni, name='university'),
path('college/', views.college, name='college'),
path('apprenticeship/', views.apprenticeship, name='apprenticeship'),
]

