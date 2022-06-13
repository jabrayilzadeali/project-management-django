from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import TodoApp
from .forms import TodoForm

# Create your views here.
def todo(request):
	todos = TodoApp.objects.all()

	try:
		user = User.objects.get(username=request.user)
		data = {
			'author': user
		}
		forms = TodoForm(initial=data)
	except:
		print('continue')
		forms = None
		
	

	if request.method == 'POST':
		if 'add_todo_item' in request.POST:
			# print(request.POST)
			# forms = TodoForm(request.POST)
			# if forms.is_valid():
			# 	forms.save()
			# 	return redirect('todo')
			todo = TodoApp.objects.create(
				author=request.user,
				task=request.POST.get('body')
			)
			return redirect('todo')

		elif 'done_todo_item' in request.POST:
			# done = TodoApp.objects.update(
			# 	done = request.POST
			# )
			print(request.POST)
			return redirect('todo')

	return render(request, 'todo/todo.html', {
		'todos': todos,
		'forms': forms
	})

def done_todo(request, pk):
	todo = TodoApp.objects.get(id=pk)
	todo.done = not todo.done
	todo.save()
	return redirect('todo')


# @login_required(login_url="login_page")
def update_todo(request, pk):
	todo = TodoApp.objects.get(id=pk)
	# todo.task

	# form = TodoForm(instance=todo)
	if request.method == "POST":
		# form = TodoForm(request.POST, instance=todo)
		# if form.is_valid():
		# 	form.save()
		# 	return redirect('todo')
		todo.task = request.POST.get('body')
		todo.save()
		return redirect('todo')
		# pass

	return render(request, 'todo/update_todo.html', {
		# 'form': form
		'task': todo.task
	})

# @login_required(login_url="login_page")
def delete_todo(request, pk):
	todo = TodoApp.objects.get(id=pk)
	if request.method == 'POST':
		todo.delete()
		return redirect('todo')
	return render(request, 'todo/delete_todo.html', {
		"todo": todo
	})
	