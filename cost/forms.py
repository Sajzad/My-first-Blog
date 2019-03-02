from django import forms
from .models import expense

class ExpenseForm(forms.ModelForm):
	class Meta:
		model=expense
		fields= '__all__'