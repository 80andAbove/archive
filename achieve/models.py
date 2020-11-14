from django.db import models
from django.contrib.auth.models import User, Permission
# Create your models here.

class Kin(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	profile_pic = models.ImageField(default="profile1.png", null=True, blank=True)
	
	def __str__(self):
		return self.name

class Category(models.Model):
	title = models.CharField(max_length=200)

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

	def __str__(self):
		return self.title