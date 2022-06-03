from django.forms import ModelForm
from .models import TodoApp

class TodoForm(ModelForm):
	class Meta:
		model = TodoApp
		fields = '__all__'