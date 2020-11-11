from django.urls import path
from . import views

urlpatterns = [
	#Welcome Page
	path('', views.welcome, name="welcome"),

	#Authentication
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),

	#User Page
	path('index/', views.index, name="index"),
	path('complete-toggle/<str:todo_id>/', views.complete_toggle, name="complete_toggle"),
	path('update-task/<str:pk>/', views.updateTask, name="update_task"),
	path('delete/<str:pk>/', views.deleteTask, name="delete"),
	path('categories/', views.categories, name="categories"),
	path('logout/', views.logoutUser, name="logout"),
]