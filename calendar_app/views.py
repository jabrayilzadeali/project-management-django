from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import CalendarApp, Comments
from .forms import CalendarForm

from datetime import date, datetime, timedelta

# Create your views here.
def get_recurrent_tasks():
	recurrent_objs = CalendarApp.objects.filter(recurrent__gte=0)
	# print(recurrent_objs)
	today = date.today()
	for recurrent_obj in recurrent_objs:
		date_added = recurrent_obj.date_added
		recurrent = recurrent_obj.recurrent
		time_delta = timedelta(days=int(recurrent))
		if today >= date_added + time_delta:
			recurrent_obj.recurrent = 0
			recurrent_obj.save()


			recurrent_obj.pk = None
			# recurrent_obj.task = 'Okay Cool'
			recurrent_obj.date_added = today
			recurrent_obj.recurrent = recurrent
			recurrent_obj.done = False
			print(recurrent_obj.done)
			if recurrent_obj.recurrent > 0:
				recurrent_obj.save()

def calendar_app(request):
	print('Getting Recurring Tasks')
	get_recurrent_tasks()
	calendar = CalendarApp.objects.all()

	# for c in calendar:
	# 	print(c.comments_set.all())
	# 	print('----------------------------------')
	# comments = CalendarApp.comments_set.all()
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
		if 'create_calendar' in request.POST:
			recurrent = request.POST.get('recurrent')
			date_added = request.POST.get('date_added')

			forms = CalendarForm(request.POST, initial=data)
			if forms.is_valid():
				forms.save(commit=False)
				forms.save()
				return redirect('calendar')
		elif 'add_comment' in request.POST:
			print('I am adding comment')
			print(request.POST)
			pk = request.POST.get('pk')

			comments = Comments.objects.create(
				author=request.user,
				description=request.POST.get('add_comment'),
				related_id = pk
			)

			return redirect('calendar')


	return render(request, 'calendar_app/calendar.html', {
		'calendar': calendar,
		'forms': forms,
		# 'comments': comments
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

def delete_calendar(request, pk):
	calendar = CalendarApp.objects.get(id=pk)
	if request.method == 'POST':
		calendar.delete()
		return redirect('calendar')
	return render(request, 'calendar_app/delete_calendar.html', {
		"calendar": calendar
	})

def update_comment(request, pk):
	comment = Comments.objects.get(id=pk)
	author = comment.author
	description = comment.description
	related_id = comment.related.id
	users = User.objects.all()
	if request.method == 'POST':
		author=request.POST.get('user')
		user = User.objects.get(username=author)
		description = request.POST.get('description')
		pk = request.POST.get('pk')
		comment.delete()
		Comments.objects.create(
			author=user,
			description=description,
			related_id = pk
		)
		return redirect('calendar')


		# comments = Comments.objects.create(
		# 	author=request.user,
		# 	description=request.POST.get('add_comment'),
		# 	related_id = pk
		# )
		
	return render(request, 'calendar_app/update_comment.html', {
		"users": users,
		"author": author,
		"description": description,
		"related_id": related_id,
	})

def delete_comment(request, pk):
	comment = Comments.objects.get(id=pk)
	if request.method == 'POST':
		comment.delete()
		return redirect('calendar')
	return render(request, 'calendar_app/delete_comment.html', {
		"comment": comment
	})