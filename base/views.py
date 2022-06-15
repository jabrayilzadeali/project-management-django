from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
def loginPage(request):
	page = 'login'
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		try:
			user = User.objects.get(username=username)
		except:
			messages.error(request, 'User not found in database')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.error(request, 'Username or password is wrong')
		
	return render(request, 'base/login_register.html', {
		'page': page
	})

def registerPage(request):
	form = UserCreationForm()
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.username = user.username.lower()
			user.save()
			login(request, user)
			return redirect('home')
		else:
			messages.error(request, 'An error occured during registration')
	return render(request, 'base/login_register.html', {
		'form': form
	})

def logoutUser(request):
	logout(request)
	return redirect('home')

def home(request):
	# return HttpResponse('okay')
	return render(request, 'base/index.html')
