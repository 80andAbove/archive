from django.contrib import admin
from .models import *

# Register your models here.


# This is for the tasks for those who are unregistered

admin.site.register(Task)
admin.site.register(Category)
