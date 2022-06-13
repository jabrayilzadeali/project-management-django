from django.forms import ModelForm
from .models import Expense, UserAmount


class UserAmountForm(ModelForm):
	class Meta:
		model = UserAmount
		fields = '__all__'


class ExpenseForm(ModelForm):
	class Meta:
		model = Expense
		fields = '__all__'
