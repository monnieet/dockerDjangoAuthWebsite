from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.homeSignIn, name='home'),
    path('signup/', views.signUp, name="signup"),
    path('signout/', views.signOut, name='signout'),
    path('viewOrEdit/<username>', views.viewAndEditProfile, name='profile'),
]