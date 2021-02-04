from django.contrib import admin
from .models import Kin, Category, Task

# Register your models here.


# This is for the tasks for those who are unregistered
from .models import *

admin.site.register(Task)
admin.site.register(Category)
