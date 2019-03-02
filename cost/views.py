from django.shortcuts import render
from .models import expense
from .forms import ExpenseForm

def my_expense(request):
	expenses= expense.objects.all()
	All= {'Expenses': expenses}
	return render(request,'Costs/expense.html', All)
	
def add_Expense(request):
	if request.method=="POST":
		form= ExpenseForm(request.POST)
		form.save()
	else:
		form= ExpenseForm
		
	return render(request,'Costs/add_expense.html', {'form':form})
	
# Create your views here.
