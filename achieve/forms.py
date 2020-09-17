from django import forms
# COMMENT: BAD PRACTICE TO IMPORT *
from .models import Task, Category
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User

class TaskForm(forms.ModelForm):
	title = forms.CharField(widget = forms.TextInput(attrs = {'placeholder':'Add new task...'}))

	class Meta:
		model = Task
		fields = '__all__'

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password', 'password2']