from django.urls import path
from . import views

urlpatterns = [
	path('', views.calendar_app, name="calendar"),
	path('done/<str:pk>', views.done_calendar, name="done_calendar"),
	path('update/<str:pk>', views.update_calendar, name="update_calendar"),
	path('delete/<str:pk>', views.delete_calendar, name="delete_calendar"),
]

