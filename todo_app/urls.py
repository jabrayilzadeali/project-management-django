from django.urls import path
from . import views

urlpatterns = [
	path('', views.todo, name="todo"),
	path('update/<str:pk>', views.update_todo, name="update_todo"),
	path('delete/<str:pk>', views.delete_todo, name="delete_todo"),
]
