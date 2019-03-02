from django.urls import path
from .import views

urlpatterns=[
path('info/', views.my_info, name='info'),
]