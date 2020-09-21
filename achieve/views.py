from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import Task, Category
from .forms import TaskForm, CreateUserForm

def welcome(request):
	return render(request, 'welcome.html')

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
	
	
	if request.method =='POST':
		form = TaskForm(request.POST)
		print('Processing Form')
		if form.is_valid():
			print('Form Valid')
			task_obj = form.save(commit=False)
			task_obj.user = request.user
			task_obj.complete = False
			task_obj.save()
		else:
			print('Form Invalid')
			print(form.errors)
		return redirect('/index')

	tasks = Task.objects.all()
	form = TaskForm()

	context = {
		'tasks':tasks, 
		'form':form,
		}
	return render(request, 'todolist.html', context)

@login_required(login_url='login')
def updateTask(request, pk):
	
	task = Task.objects.get(id=pk)	

	if request.method == 'POST':
		form = TaskForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
			return redirect('/index')

	form = TaskForm(instance=task)
	context = {'form':form}

	return render(request, 'update.html', context)

@login_required(login_url='login')
def deleteTask(request, pk):
	item = Task.objects.get(id=pk)

	if request.method == 'POST':
		item.delete()
		return redirect('/index')

	context = {
		'item':item,
		}
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
