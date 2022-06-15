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

	# for user in users:
	# 	user_amount = UserAmount.objects.get(user=user)



	if request.method == 'POST':
		# print('-----------------------------------------------------')
		# print(request.POST)
		# print('-----------------------------------------------------')
		name = request.POST.get('name')
		price = request.POST.get('price')
		count = request.POST.get('count')
		selected_users = request.POST.getlist('select-user')
		paid = request.POST.getlist('paid')

		# print(selected_users)
		# print(paid)

		all_users_who_paid = []
		for user, paid in zip(selected_users, paid):
			# print(user, paid)
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
	total_user_paid = []
	total_user_paid.clear()
	for user in users:
		my_paid_user = UserAmount.objects.filter(user=user)
		# print(my_paid_user)
		if my_paid_user:
			total = 0
			for my_user in my_paid_user:
				total += my_user.pay
			total_user_paid.append({'user': my_paid_user.first().user, 'total': total})

	# print(total_user_paid)
	# print('------------------------<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')

	# print(user_amount)
	return render(request, 'expense_tracker_app/expense_tracker.html', {
		'expenses': expenses,
		'user_amount': user_amount,
		'forms': forms,
		'user_amount_forms': user_amount_forms,
		'users': users,
		'total_user_paid': total_user_paid
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
		total_user_paid = []

		print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
		print(who_paid)
		print(type(who_paid))
		# print(users)
		# print(users_paid)
		# print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
		# for paid_user in who_paid:
		# 	for user, paid in zip(users, users_paid):
		# 		print(f'>>>{paid_user.user}>>>>>>>>>>>>>>>>>>>>{user}>>>>>>>>>>>')
		# 		if paid_user.user == user:
		# 			paid_user.pay = paid
		# 			print(paid_user)
		# 			paid_user.save()



		expense.who_paid.all().delete()
		# expense.who_paid.clear()
		all_users_who_paid_updated = []
		for user, paid in zip(users, users_paid):
			user_paid = UserAmount.objects.create(
				user = User.objects.get(username=user),
				pay = paid
			)

			all_users_who_paid_updated.append(user_paid)

		for paid in all_users_who_paid_updated:
			expense.who_paid.add(paid)

		expense.save()

		# print(name, price, count, users, users_paid)
		return redirect('expense_tracker')


	return render(request, 'expense_tracker_app/update_expense_tracker.html', {
		'expense': expense,
		'who_paid_first': who_paid[0],
		'who_paid_except_first': who_paid[1:],
		'users': users,
	})

def delete_expense_tracker(request, pk):
	expense = Expense.objects.get(id=pk)
	total_user_paid = []

	if request.method == 'POST':
		expense.who_paid.all().delete()
		print(expense.who_paid.all())
		expense.delete()
		return redirect('expense_tracker')

	who_paid = expense.who_paid.all()
	return render(request, 'expense_tracker_app/delete_expense_tracker.html', {
		'expense': expense,
		'who_paid': who_paid,
		'total_user_paid': total_user_paid
	})


# Ali  Islam     price  
#   2     10        12
#   5     15        20
#
#
# 2 --> 10 - 2 = 8
# 1 --> 15 - 5 = 10 
# 8 + 10 = 18

# 2 + 5 = 7
# 10 + 15 = 25
# 25 - 7 = 18