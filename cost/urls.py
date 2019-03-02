from django.urls import path
from .import views

urlpatterns=[
path('list/', views.my_expense, name='cost-list'),
path('add-expense/', views.add_Expense, name='add_Expense'),

]