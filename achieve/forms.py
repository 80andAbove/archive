from django import forms
# COMMENT: BAD PRACTICE TO IMPORT *
from .models import Task, Category
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User

class TaskForm(forms.ModelForm):
	title = forms.CharField(widget = forms.TextInput(attrs = {'placeholder':'Add new task...'}))

	class Meta:
		model = Task
		fields = ['title']

class CreateUserForm(UserCreationForm):
	email = forms.EmailField(widget=forms.TextInput, label="Email")
	password1 = forms.CharField(widget=forms.PasswordInput, label="Password")
	password2 = forms.CharField(widget=forms.PasswordInput, label="Password (again)")
	
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

