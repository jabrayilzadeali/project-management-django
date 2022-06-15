from django.urls import path
from . import views

urlpatterns = [
	path('login', views.loginPage, name="login_page"),
	path('register', views.registerPage, name="register_page"),
	path('logout', views.logoutUser, name="logout_user"),
	path('', views.home, name="home"),
]