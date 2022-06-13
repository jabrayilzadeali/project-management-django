from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Expense, UserAmount
from .forms import ExpenseForm, UserAmountForm

# Create your views here.
def expense_tracker_app(request):
	users = User.objects.all()
	expenses = Expense.objects.all()
	try:
		user = User.objects.get(username=request.user)
		data = {
			'author': user
		}
		user_amount_forms = UserAmountForm
		forms = ExpenseForm(initial=data)

	except:
		user_amount_forms = None
		forms = None

	if request.method == 'POST':
		print('-----------------------------------------------------')
		print(request.POST)
		print('-----------------------------------------------------')
		name = request.POST.get('name')
		price = request.POST.get('price')
		count = request.POST.get('count')
		selected_users = request.POST.getlist('select-user')
		paid = request.POST.getlist('paid')

		print(selected_users)
		print(paid)

		all_users_who_paid = []
		for user, paid in zip(selected_users, paid):
			print(user, paid)
			user_paid = UserAmount.objects.create(
				user = User.objects.get(username=user),
				pay = paid
			)

			all_users_who_paid.append(user_paid)

		expense = Expense.objects.create(
			name = name,
			price = price,
			count = count,
		)

		for paid in all_users_who_paid:
			expense.who_paid.add(paid)
		
		return redirect('expense_tracker')

	user_amount = UserAmount.objects.all()
	return render(request, 'expense_tracker_app/expense_tracker.html', {
		'expenses': expenses,
		'user_amount': user_amount,
		'forms': forms,
		'user_amount_forms': user_amount_forms,
		'users': users
	})


def update_expense_tracker(request, pk):
	users = User.objects.all()
	expense = Expense.objects.get(id=pk)
	who_paid = expense.who_paid.all()
	if request.method == 'POST':
		name = request.POST.get('name')
		price = request.POST.get('price')
		count = request.POST.get('count')
		users = request.POST.getlist('select-user')
		users_paid = request.POST.getlist('paid')
		expense.name = name
		expense.price = price
		expense.count = count

		print(who_paid, '-------------------')

		expense.who_paid.clear()

		all_users_who_paid_updated = []
		for user, paid in zip(users, users_paid):
			print(user, paid)
			user_paid = UserAmount.objects.create(
				user = User.objects.get(username=user),
				pay = paid
			)

			all_users_who_paid_updated.append(user_paid)

		for paid in all_users_who_paid_updated:
			expense.who_paid.add(paid)

		expense.save()

		print(name, price, count, users, users_paid)
		return redirect('expense_tracker')


	return render(request, 'expense_tracker_app/update_expense_tracker.html', {
		'expense': expense,
		'who_paid_first': who_paid[0],
		'who_paid_except_first': who_paid[1:],
		'users': users
	})

def delete_expense_tracker(request, pk):
	expense = Expense.objects.get(id=pk)

	if request.method == 'POST':
		expense.who_paid.all().delete()
		print(expense.who_paid.all())
		expense.delete()
		return redirect('expense_tracker')

	who_paid = expense.who_paid.all()
	return render(request, 'expense_tracker_app/delete_expense_tracker.html', {
		'expense': expense,
		'who_paid': who_paid
	})


# Ali  Islam     price  
#   5      9        14
#
#
# 9 -5 = 4 Ali Islama 4 borcludur