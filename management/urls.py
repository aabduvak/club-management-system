from django.urls import path

from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index-page'),
    path('signup/', views.Signup.as_view(), name='signup-page'),
    path('signin/', views.Signin.as_view(), name='signin-page'),
    path('reset/', views.ForgotPassword.as_view(), name='reset-page'),
]
