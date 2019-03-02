from django.urls import path
from .import views

urlpatterns=[
path('Districts/', views.district_list, name='districts'),
path('Divisions/', views.division_list, name='divisions'),
path('dists/<int:div_id>/', views.dists_of_division, name='dists-of-div'),


]