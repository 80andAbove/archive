from django.db import models
from django.contrib.auth.models import User

# Create your models here.

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

	def __str__(self):
		return self.title