from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	# return HttpResponse('okay')
	return render(request, 'base/index.html')
