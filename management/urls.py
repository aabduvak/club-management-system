from django.urls import path

from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index-page'),
    path('signup/', views.Signup.as_view(), name='signup-page'),
    path('signin/', views.Signin.as_view(), name='signin-page'),
    path('reset/', views.ForgotPassword.as_view(), name='reset-page'),
    path('profile/', views.Account.as_view(), name='profile-page'),
    path('settings/', views.Maintenance.as_view(), name='settings-page'),
    path('myclubs/', views.MyClubs.as_view(), name='myclubs-page'),
    path('events/', views.Events.as_view(), name='events-page'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('events/<slug:slug>', views.EventDetail.as_view(), name='event-page'),
]
