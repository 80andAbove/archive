from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm 

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .forms import *


def registerPage(request):
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, 'Account was created for ' + user)
		return redirect('login')

	context = {'form':form}
	return render(request, 'register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('index')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('index')
			else:
				messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
def index(request):
	tasks = Task.objects.all()
	
	form = TaskForm()
	
	if request.method =='POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/')


	context = {'tasks':tasks, 'form':form}
	return render(request, 'todolist.html', context)

@login_required(login_url='login')
def updateTask(request, pk):
	task = Task.objects.get(id=pk)
	
	form = TaskForm(instance=task)
	
	if request.method == 'POST':
		form = TaskForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}

	return render(request, 'update.html', context)

@login_required(login_url='login')
def deleteTask(request, pk):
	item = Task.objects.get(id=pk)

	if request.method == 'POST':
		item.delete()
		return redirect('/')

	context = {'item':item}
	return render(request, 'delete.html', context)

@login_required(login_url='login')
def categories(request):
	category = Category.objects.all()

	context = {'category': category}
	return render(request, 'categories.html', context)


"""
	categoryForm = CategoryForm(instance=task)

	if request.method == 'POST':
		categoryForm = CategoryForm(request.POST)
		if categoryForm.is_valid():
			categoryForm.save()
		return redirect('/')
"""
