from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TodoApp(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	task = models.CharField(max_length=200)
	updated = models.DateTimeField(auto_now=True) 
	created = models.DateTimeField(auto_now_add=True)
	done = models.BooleanField(default=False)

	class Meta:
		ordering = ['-updated', '-created']

	def __str__(self):
		return self.task


