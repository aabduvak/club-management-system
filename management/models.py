from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Role(models.Model):
	title = models.CharField(max_length=100)	

	def __str__(self):
		return f'{self.title}'

class User(models.Model):
	gender_choices = [("MALE", "Male"), ("FEMALE", "Female")]	
	
	name = models.CharField(max_length=100)
	surname = models.CharField(max_length=100)
	studentID = models.CharField(max_length=9)
	gender = models.CharField(max_length=10, choices=gender_choices)
	email = models.EmailField(max_length=200)
	password = models.CharField(max_length=100)
	role = models.ForeignKey(Role, on_delete=models.SET_NULL, related_name="roles", null=True)
		
	def __str__(self):
		return f'{self.name} {self.surname} | {self.studentID}'

class Event(models.Model):
	title = models.CharField(max_length=200)
	short_desc = models.CharField(max_length=400)
	long_desc = models.TextField()
	img = models.ImageField(upload_to='posts')
	date = models.DateTimeField(auto_now_add= True,verbose_name="Date")
	content = RichTextField()
	
	