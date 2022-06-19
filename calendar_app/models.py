from django.db import models
# from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class CalendarApp(models.Model):
	task = models.CharField(max_length=200)
	# Add default value request.user okay to author
	author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="for_who")
	for_who = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="author")
	date_added = models.DateField(blank=True, null=True)
	time_start = models.TimeField(blank=True, null=True)
	time_finish = models.TimeField(blank=True, null=True)
	done = models.BooleanField(default=False)
	recurrent = models.IntegerField(default=0)

	def __str__(self):
		return f'{self.task}, {self.author}'

class Comments(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	description = models.CharField(max_length=200)
	updated = models.DateTimeField(auto_now=True) 
	created = models.DateTimeField(auto_now_add=True)
	related = models.ForeignKey(CalendarApp, on_delete=models.CASCADE)

	def __str__(self):
		return f'author: {self.author} | description: {self.description}'