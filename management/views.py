from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
class Index(View):
	def get(self, request):
		#if request.user.is_authenticated:
		return render(request, 'management/index.html')
		#return redirect(reverse('signin-page'))
		
class Signup(View):
	def get(self, request):
		return render(request, 'management/signup.html')
		
class Signin(View):
	def get(self, request):
		return render(request, 'management/signin.html')

class ForgotPassword(View):
	def get(self, request):
		return render(request, 'management/reset.html')

class Account(View):
	def get(self, request):
		return render(request, 'management/profile.html')

class Maintenance(View):
	def get(self, request):
		return render(request, 'management/maintenance.html')

class MyClubs(View):
	def get(self, request):
		return render(request, 'management/my_clubs.html')

class Events(View):
	def get(self, request):
		return render(request, 'management/events.html')

def logout(request):
    django_logout(request)
    return redirect(f'http://localhost:8000/signin')

def page_not_found(request, exception):
    return render(request, '404.html', status=404)