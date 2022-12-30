from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from .models import User, Role

# Create your views here.

class Index(View):
	def get(self, request):
		studentID = request.session.get('id')
		if (studentID is not None):
			user = User.objects.get(studentID=studentID)
			
			context = {
				'user': user,
			}
			return render(request, 'management/index.html', context)
		return redirect(reverse('signin-page'))
		
		
class Signup(View):
	def get(self, request):
		return render(request, 'management/signup.html')
		
	def post(self, request):
		
		id = request.POST.get('studentID')
		is_exist = User.objects.filter(studentID=id).exists()
		if is_exist is False:
			password = request.POST.get('password')
			name = request.POST.get('firstName')
			surname = request.POST.get('lastName')
			email = request.POST.get('email')
						
			user = User(first_name=name, last_name=surname,email=email, password=password, studentID=id)
			user.save()
			
			request.session['id'] = id
			return redirect(reverse('index-page'))
		
		return redirect(reverse('signup-page'))
		
class Signin(View):
	def post(self, request):
		id = request.POST.get('studentID')
		password = request.POST.get('password')
		
		is_exist = User.objects.filter(studentID=id, password=password).exists()
		if is_exist is True:
			
			request.session['id'] = id
			return redirect(reverse('index-page'))
		return redirect(reverse('signin-page'))
	
	def get(self, request):
		return render(request, 'management/signin.html')

class ForgotPassword(View):
	def get(self, request):
		return render(request, 'management/reset.html')

class Account(View):
	def get(self, request):
		studentID = request.session.get('id')
		
		if (studentID is not None):
			user = User.objects.get(studentID=studentID)
            
			context = {
                'user': user,
            }
			return render(request,'management/profile.html', context)
		return redirect(reverse('signin-page'))
	
	def post(self, request):
		studentID = request.session.get('id')
		
		user = User.objects.get(studentID=studentID)
		if 'photo' in request.FILES:
			user.photo = request.FILES['photo']
		user.first_name = request.POST.get('first_name')
		user.last_name = request.POST.get('last_name')
		user.email = request.POST.get('email')
		
		user.save()
		return redirect(reverse('profile-page'))
        

class Maintenance(View):
	def get(self, request):
		return render(request, 'maintenance.html')

class MyClubs(View):
	def get(self, request):
		return render(request, 'management/my_clubs.html')

class Events(View):
	def get(self, request):
		return render(request, 'management/events.html')

class Event(View):
	def get(self, request, slug):
		return render(request, 'management/event.html')

def logout(request):
    return redirect(reverse('signin-page'))

def page_not_found(request, exception):
    return render(request, '404.html', status=404)

def permission_denied(request, exception):
    return render(request, '403.html', status=403)