from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

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

def page_not_found(request, exception):
    return render(request, '404.html', status=404)