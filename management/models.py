from django.db import models
from django.utils.text import slugify
from django.urls import reverse

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

class Club(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField()
	img = models.ImageField(upload_to='clubs')
	leader = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='leader', blank=True, null=True)
	users = models.ManyToManyField(User, related_name='clubs', blank=True)
	slug = models.SlugField(unique=True, blank=True, default='', null=False)
	
	def get_absolute_url(self):
		return reverse('club-page', args=[self.slug])
	
	def save(self, *args, **kwargs):
		if not self.slug:
            # Generate a slug from the title if the slug is not set
			self.slug = slugify(self.name)
			super().save(*args, **kwargs)
	
	def __str__(self):
		return f'{self.name}'

class Event(models.Model):
	title = models.CharField(max_length=200)
	short_desc = models.TextField()
	long_desc = models.TextField()
	img = models.ImageField(upload_to='posts')
	date = models.DateTimeField(auto_now_add= True,verbose_name="Date")
	club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='clubs', null=True)
	place = models.CharField(max_length=200, default='')
	users = models.ManyToManyField(User, related_name='events', blank=True)
	slug = models.SlugField(unique=True, blank=True, default='', null=False)
	
	def get_absolute_url(self):
		return reverse('event-page', args=[self.slug])

	def save(self, *args, **kwargs):
		if not self.slug:
            # Generate a slug from the title if the slug is not set
			self.slug = slugify(self.title)
			super().save(*args, **kwargs)
	
	def __str__(self):
		return f'{self.title} | {self.club}'

class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
	entered_text = models.TextField(max_length=400)
	club = models.ForeignKey(Club, on_delete=models.CASCADE,
                             related_name='comments')
	datetime = models.DateTimeField(auto_now_add=True, null=True)
	
	def __str__(self):
		return f'Comment by {self.user} on {self.club} at {self.datetime}'