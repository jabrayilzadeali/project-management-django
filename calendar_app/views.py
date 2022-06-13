from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import CalendarApp
from .forms import CalendarForm

# Create your views here.
def calendar_app(request):
	calendar = CalendarApp.objects.all()
	try:
		user = User.objects.get(username=request.user)
		data = {
			'author': user
		}
		forms = CalendarForm(initial=data)

	except:
		forms = None
	# forms = CalendarForm()
	# user = request.user
	# forms.author = user

	if request.method == 'POST':
		forms = CalendarForm(request.POST, initial=data)
		if forms.is_valid():
			forms.save(commit=False)
			forms.save()
			return redirect('calendar')

	return render(request, 'calendar_app/calendar.html', {
		'calendar': calendar,
		'forms': forms,
		# 'user': user
	})

# @login_required(login_url="login_page")
def update_calendar(request, pk):
	calendar_task = CalendarApp.objects.get(id=pk)

	form = CalendarForm(instance=calendar_task)
	if request.method == "POST":
		form = CalendarForm(request.POST, instance=calendar_task)
		if form.is_valid():
			form.save(commit=False)
			form.author = request.user
			form.save()
			return redirect('calendar')
		return redirect('calendar')
		# pass

	return render(request, 'calendar_app/update_calendar.html', {
		'form': form
	})

def done_calendar(request, pk):
	calendar_task = CalendarApp.objects.get(id=pk)
	calendar_task.done = not calendar_task.done
	calendar_task.save()
	return redirect('calendar')

def delete_celandar(request, pk):
	pass

def delete_calendar(request, pk):
	calendar = CalendarApp.objects.get(id=pk)
	if request.method == 'POST':
		calendar.delete()
		return redirect('calendar')
	return render(request, 'calendar_app/delete_calendar.html', {
		"calendar": calendar
	})