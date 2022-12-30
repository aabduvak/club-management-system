from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from .models import User, Role, Event, Club

# Create your views here.

class Index(View):
	def get(self, request):
		studentID = request.session.get('id')
		if (studentID is not None):
			user = User.objects.get(studentID=studentID)
			events = Event.objects.order_by('-id')[:9]
			context = {
				'user': user,
				'events': events
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
			is_leader = Club.objects.filter(leader=user).exists()
			if (is_leader):
				club = Club.objects.get(leader=user)
			
			context = {
                'user': user,
				'club': club,
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
		studentID = request.session.get('id')
		
		if (studentID is not None):
			user = User.objects.get(studentID=studentID)
			events = user.events.order_by('-id')[:9]
			
			context = {
                'user': user,
				'events': events
            }
			return render(request,'management/events.html', context)
		return redirect(reverse('signin-page'))

class EventDetail(View):
	def get(self, request, slug):
		studentID = request.session.get('id')
		
		if (studentID is not None):
			event = Event.objects.get(slug=slug)
			user = User.objects.get(studentID=studentID)
			
			joined = event.users.filter(studentID=studentID)
			context = {
				'event': event,
				'user': user,
				'joined': joined
			}
			return render(request, 'management/event.html', context)
		return redirect(reverse('signin-page'))
	
	def post(self, request, slug):
		studentID = request.session.get('id')
		if (studentID is not None):
			event = Event.objects.get(slug=slug)
			user = User.objects.get(studentID=studentID)
			event.users.add(user)
			event.save()
			
			context = {
                'user': user,
				'event': event,
				'joined': True
            }
			return render(request,'management/event.html', context)
		return redirect(reverse('signin-page'))
			

class Logout(View):
    def get(self, request):
        request.session.clear()
        return redirect(reverse('signin-page'))

def page_not_found(request, exception):
    return render(request, '404.html', status=404)

def permission_denied(request, exception):
    return render(request, '403.html', status=403)