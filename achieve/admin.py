from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Kin, Category, Task
from django.urls import path
from django.http import HttpResponseRedirect

# Register your models here.


# This is for the tasks for those who are unregistered
from .models import *

admin.site.register(Task)
admin.site.register(Category)
