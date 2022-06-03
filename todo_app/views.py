from django.shortcuts import render, redirect
from .models import TodoApp
from .forms import TodoForm

# Create your views here.
def todo(request):
	todos = TodoApp.objects.all()
	forms = TodoForm()
	if request.method == 'POST':
		print(request.POST)
		forms = TodoForm(request.POST)
		if forms.is_valid():
			forms.save()
			return redirect('todo')

	return render(request, 'todo/todo.html', {
		'todos': todos,
		'forms': forms
	})

def update_todo(request, pk):
	todo = TodoApp.objects.get(id=pk)
	form = TodoForm(instance=todo)
	if request.method == "POST":
		form = TodoForm(request.POST, instance=todo)
		if form.is_valid():
			form.save()
			return redirect('todo')
	return render(request, 'todo/update_todo.html', {
		'form': form
	})

def delete_todo(request, pk):
	todo = TodoApp.objects.get(id=pk)
	if request.method == 'POST':
		todo.delete()
		return redirect('todo')
	return render(request, 'todo/delete_todo.html', {
		"todo": todo
	})
	