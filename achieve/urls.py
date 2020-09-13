from django.urls import path
from . import views

urlpatterns = [
	#Guest page
	path('', views.index, name="index"),
	path('update_task/<str:pk>/', views.updateTask, name="update_task"),
	path('delete/<str:pk>/', views.deleteTask, name="delete"),
	path('categories/', views.categories, name="categories"),

	#User login page
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login")
]