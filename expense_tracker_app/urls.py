from django.urls import path
from . import views

urlpatterns = [
	path('', views.expense_tracker_app, name="expense_tracker"),
	path('update/<str:pk>', views.update_expense_tracker, name="update_expense_tracker"),
	path('delete/<str:pk>', views.delete_expense_tracker, name="delete_expense_tracker"),
]
