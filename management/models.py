from django.db import models
# Create your models here.

class Role(models.Model):
	title = models.CharField(max_length=100)	

	def __str__(self):
		return f'{self.title}'

class User(models.Model):
	gender_choices = [("MALE", "Male"), ("FEMALE", "Female")]	
	
	studentID = models.CharField(max_length=9, unique=True)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	gender = models.CharField(max_length=10, choices=gender_choices, default='MALE')
	email = models.EmailField(max_length=200)
	password = models.CharField(max_length=100)
	role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name="roles", null=True)
	photo = models.ImageField(upload_to='users', null=True)
	
	def __str__(self):
		return f'{self.first_name} {self.last_name} | {self.studentID}'
		
	def get_absolute_url(self):
		return "/users/%i/" % (self.pk)

class Event(models.Model):
	title = models.CharField(max_length=200)
	short_desc = models.CharField(max_length=400)
	long_desc = models.TextField()
	img = models.ImageField(upload_to='posts')
	date = models.DateTimeField(auto_now_add= True,verbose_name="Date")
	