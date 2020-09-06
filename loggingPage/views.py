# loggingPage/views.py

from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from datetime import datetime
from .forms import SignUpForm, SignInForm, UpdateEmailForm
from django.contrib.auth.models import User


def homeSignIn(request):
	errorAuth = False
	if request.method == 'POST':
		form = SignInForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('profile', username=user.username)
			else:
				errorAuth = True
	else:
		form = SignInForm()
	return render(request, 'loggingPage/base.html.twig', {'errorAuth': errorAuth, 'form': form})


def signUp(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=password)
			login(request, user)
			return redirect('profile', username=user.username)
	else:
		form = SignUpForm()
	return render(request, 'loggingPage/signUp.html.twig', {'form': form})


def signOut(request):
	auth.logout(request)
	return render(request, 'loggingPage/signOut.html.twig')


def viewAndEditProfile(request, username):
	
	user = User.objects.get(username=username)

	if request.method == 'POST':
		form = UpdateEmailForm(request.POST)
		if form.is_valid():
			user.email = form.cleaned_data.get('email')
			user.save()
			form = UpdateEmailForm()
			return render(request, 'loggingPage/loggedUser.html.twig', {'user': user, 'form': form})

	else:
		form = UpdateEmailForm()

	return render(request, 'loggingPage/loggedUser.html.twig', {'user': user, 'form': form})