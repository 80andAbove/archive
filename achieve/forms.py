from django import forms
# COMMENT: BAD PRACTICE TO IMPORT *
from .models import Task, Category, Kin
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User

class TaskForm(forms.ModelForm):

	title = forms.CharField(widget = forms.TextInput(attrs = 
	{
		'placeholder':'Add new task...',
		"class": "form-control"
	}
	))

	category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs=
		{
			"class": "selectpicker",
			'placeholder':'Category',
		}
	))

	description = forms.CharField(
		required=False,
		widget = forms.Textarea(attrs = 
		{
        	"class": "form-control",
			'placeholder':'Add description...',
			"rows": 4,

		}
	))

	class Meta:
		model = Task
		fields = ['title', 'category', 'description']

class CategoryForm(forms.ModelForm):
	title = forms.CharField(widget = forms.TextInput(attrs=
	{
		'placeholder': 'Add new category...',
		"class": "form-control",
	}
	))	

	class Meta:
		model = Category
		fields = ['category']

class CreateUserForm(UserCreationForm):
	email = forms.EmailField(widget=forms.TextInput, label="Email")
	password1 = forms.CharField(widget=forms.PasswordInput, label="Password")
	password2 = forms.CharField(widget=forms.PasswordInput, label="Password (again)")
	
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
	name = forms.CharField(widget = forms.TextInput(attrs=
	{
		'placeholder': 'Input your name...',
		"class": "form-control",
	}
	))
	
	age = forms.CharField(widget = forms.TextInput(attrs=
	{
		'placeholder': "What's your age?",
		"class": "form-control",
	}
	))

	class Meta:
		model = Kin
		fields = ['name', 'age', 'family_role']