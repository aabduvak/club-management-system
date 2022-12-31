from datetime import datetime
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.utils.text import slugify


from .models import User, Role, Event, Club, Comment

# Create your views here.

class Index(View):
	def get(self, request):
		studentID = request.session.get('id')
		if (studentID is not None):
			user = User.objects.get(studentID=studentID)
			events = Event.objects.order_by('-id')[:9]
			clubs = Club.objects.order_by('name')
			
			is_leader = Club.objects.filter(leader=user).exists()
			club = None
			if (is_leader):
				club = Club.objects.get(leader=user)
							
			context = {
				'user': user,
				'events': events,
				'clubs': clubs,
				'club': club,
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
			club = None
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
		studentID = request.session.get('id')
		
		if (studentID is not None):
			user = User.objects.get(studentID=studentID)
			my_clubs = user.clubs.order_by('-name')
			clubs = Club.objects.exclude(users=user)
			is_leader = Club.objects.filter(leader=user).exists()
			club = None
			if (is_leader):
				club = Club.objects.get(leader=user)
			context = {
                'user': user,
				'my_clubs': my_clubs,
				'other_clubs': clubs,
				'club': club,
            }
		
		return render(request, 'management/clubs.html', context)

class Events(View):
	def get(self, request):
		studentID = request.session.get('id')
		
		if (studentID is not None):
			user = User.objects.get(studentID=studentID)
			events = user.events.order_by('-id')[:9]
			
			is_leader = Club.objects.filter(leader=user).exists()
			club = None
			if (is_leader):
				club = Club.objects.get(leader=user)
			context = {
                'user': user,
				'events': events,
				'club': club,
            }
			return render(request,'management/events.html', context)
		return redirect(reverse('signin-page'))

class EventDetail(View):
	def get(self, request, slug):
		studentID = request.session.get('id')
		
		if (studentID is not None):
			event = Event.objects.get(slug=slug)
			user = User.objects.get(studentID=studentID)
			context = {
				'event': event,
				'user': user,
				'club': event.club
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
				'event': event
            }
			return render(request,'management/event.html', context)
		return redirect(reverse('signin-page'))
			
class Logout(View):
    def get(self, request):
        request.session.clear()
        return redirect(reverse('signin-page'))

class ClubDetail(View):
	def get(self, request, slug):
		studentID = request.session.get('id')
		
		if (studentID is not None):
			user = User.objects.get(studentID=studentID)
			club = Club.objects.get(slug=slug)
			comments = Comment.objects.all()
			context = {
				'club': club,
				'user': user,
				'comments': comments
			}
			return render(request, 'management/club.html', context)
		return redirect(reverse('signin-page'))
	
	def post(self, request, slug):
		studentID = request.session.get('id')
		
		if (studentID is not None):
			user = User.objects.get(studentID=studentID)
			club = Club.objects.get(slug=slug)
			comment = Comment.objects.create(entered_text=request.POST.get('entered_text'), club=club, user=user)
			
			comment.save()
			
			return redirect(reverse('club-page', args=[slug]))
		return redirect(reverse('signin-page'))

class ClubJoinView(View):
	def get(self, request, slug):
		studentID = request.session.get('id')
		
		if (studentID is not None):
			user = User.objects.get(studentID=studentID)
			club = Club.objects.get(slug=slug)
			
			if user not in club.users.all():
				club.users.add(user)
				club.save()
			return redirect(reverse('club-page', args=[slug]))
		return redirect(reverse('signin-page'))

class ClubLeaveView(View):
	def get(self, request, slug):
		studentID = request.session.get('id')
		
		if (studentID is not None):
			user = User.objects.get(studentID=studentID)
			club = Club.objects.get(slug=slug)
			
			if user in club.users.all():
				club.users.remove(user)
				if user == club.leader:
					Club.objects.filter(slug=slug).update(leader=None)
					user.role = None
					user.save()
				club.save()
			return redirect(reverse('clubs-page'))
		return redirect(reverse('signin-page'))
	
class CreateEventView(View):
	def get(self, request, slug):
		studentID = request.session.get('id')
		
		if (studentID is not None):
			user = User.objects.get(studentID=studentID)
			club = Club.objects.get(slug=slug)
			context = {
				'club': club,
				'user': user,
			}
			if user == club.leader:
				return render(request, 'management/create_event.html', context)
			else:
				return redirect(reverse('index-page'))
		return redirect(reverse('signin-page'))
	
	def post(self, request, slug):
		studentID = request.session.get('id')
		
		if (studentID is not None):
			user = User.objects.get(studentID=studentID)
			club = Club.objects.get(slug=slug)
			
			if user == club.leader:
				title = request.POST.get('title')
				place = request.POST.get('place')
				date = request.POST.get('date')
				short = request.POST.get('short_descr')
				long = request.POST.get('long_descr')
				slug = slugify(title)
				if 'img' in request.FILES:
					img = request.FILES['img']
				
				event = Event.objects.create(title=title, place=place, date=date, short_desc=short, long_desc=long, img=img, club=club)
				event.users.add(user)
				event.save()
				
				return redirect(reverse('events-page'))
			else:
				return redirect(reverse('index-page'))
		return redirect(reverse('signin-page'))
	
class DeleteEventView(View):
	def post(self, request, slug):
		studentID = request.session.get('id')
		
		if (studentID is not None):
			user = User.objects.get(studentID=studentID)
			event = Event.objects.get(slug=slug)
			
			if event and user == event.club.leader:
				event.delete()
			return redirect(reverse('index-page'))
		return redirect(reverse('signin-page'))
	
	def get(self, request, slug):
		return render(request, '405.html', status=405)



def page_not_found(request, exception):
    return render(request, '404.html', status=404)

def permission_denied(request, exception):
    return render(request, '403.html', status=403)