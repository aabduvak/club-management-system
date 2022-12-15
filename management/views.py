from django.shortcuts import render
from django.views import View

# Create your views here.
class Index(View):
	def get(self, request):
		return render(request, 'management/index.html')
		
class Signup(View):
	def get(self, request):
		return render(request, 'management/signup.html')
		
class Signin(View):
	def get(self, request):
		return render(request, 'management/signin.html')

class ForgotPassword(View):
	def get(self, request):
		return render(request, 'management/reset.html')