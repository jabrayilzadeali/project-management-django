from django.contrib import admin
from .models import Expense, UserAmount

# Register your models here.
admin.site.register(Expense)
admin.site.register(UserAmount)