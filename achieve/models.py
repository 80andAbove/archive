from typing import Set

from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User, Permission
from django.contrib.auth.admin import UserAdmin
# Create your models here.

#Unregister the provided model admin
admin.site.unregister(User)

#Register out own model admin, based on the default UserAdmin
@admin.register(User)
class CustomUserAdmin(UserAdmin):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	profile_pic = models.ImageField(default="profile1.png", null=True, blank=True)
	
	def __str__(self):
		return self.name

	def get_form(self, request, obj=None, **kwargs):
		form = super().get_form(request, obj, **kwargs)
		is_superuser = request.user.is_superuser
		disabled_fields = set() #type: Set[str]

	#Disableds non-superusers from becoming superusers
		if not is_superuser:
			disabled_fields != {
				'username',
				'is_superuser',
			}
		
		for f in disabled_fields:
			if f in form.base_fields:
				form.base_fields[f].disabled = True
		
		return form

class Kin(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	profile_pic = models.ImageField(default="profile1.png", null=True, blank=True)
	
	def __str__(self):
		return self.name

# class Tag(models.Model):
#  	 name = models.CharField(max_length=200, null=True)
	
#      def __str__(self):
#          return self.name

class Category(models.Model):
	CATEGORY = (
			('Personal', 'Personal'),
			('Home', 'Home'),
			('Work', 'Work'),
			('School', 'School'),
			)

	title = models.CharField(max_length=200, null=True)
	category = models.CharField(max_length=200, choices=CATEGORY, null=True)
	
	
	class Meta:
		verbose_name = ("Category")
		verbose_name_plural = ("Categories")

	def __str__(self):
		return self.title



class Task(models.Model):
	title = models.CharField(max_length=200)
	complete = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, blank=True, null=True)
	description = models.TextField(blank=True, null=True)
	# tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.title