from django.shortcuts import render

# Create your views here.
def expense_tracker_app(request):
	return render(request, 'expense_tracker_app/expense_tracker.html')