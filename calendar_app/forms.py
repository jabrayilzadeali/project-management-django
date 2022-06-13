from django import forms
from django.forms import ModelForm
from .models import CalendarApp


class DateInput(forms.DateInput):
	input_type = 'date'


class TimeInput(forms.TimeInput):
	input_type = 'time'


class CalendarForm(ModelForm):
	class Meta:
		model = CalendarApp
		fields = ['author', 'task', 'for_who', 'date_added', 'time_start', 'time_finish']
		widgets = {
			'date_added': DateInput(),
			'time_start': TimeInput(),
			'time_finish': TimeInput(),
		}