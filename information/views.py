from django.shortcuts import render
from .models import Districts, Divisions


def district_list(request):
	districts=Districts.objects.all()
	context={'districts':districts}
	return render(request, 'Information/districts.html',context)
	
def division_list(request):
	divisions= Divisions.objects.all()
	context={'divisions':divisions}
	return render(request,'information/division_list.html',context)
	
def dists_of_division(request, div_id):
	division= Divisions.objects.get(pk=div_id)
	districts= Districts.objects.filter(division=division)
	context={ 'districts':districts, 'division':division}
	return render(request, 'information/dists.html', context) 
	
	
	
# Create your views here.
