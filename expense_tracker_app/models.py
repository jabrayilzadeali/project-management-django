from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserAmount(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	pay = models.DecimalField(max_digits=10, decimal_places=True, default=0)


	def __str__(self):
		return f"user: {self.user} | paid: {self.pay} | expenses: {self.expenses.all()}"


class Expense(models.Model):
	# https://stackoverflow.com/questions/54005084/condition-in-model-django
	name = models.CharField(max_length=200)
	price = models.DecimalField(max_digits=10, decimal_places=True)
	
	count = models.IntegerField(default=0)
	updated = models.DateTimeField(auto_now=True) 
	created = models.DateTimeField(auto_now_add=True)

	who_paid = models.ManyToManyField(UserAmount, related_name="expenses")

	def total(self):
		return self.price * self.count

	def __str__(self):
		return f"item_name: {self.name} | price: {self.price}"