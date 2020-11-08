from django import forms
# COMMENT: BAD PRACTICE TO IMPORT *
from .models import Task, Category
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

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password', 'password2']