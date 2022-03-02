from django.shortcuts import  render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

def logout_request(request):
	logout(request)
	return redirect("homepage")

def register_request(request):
	form = RegisterForm()

	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect("../")
	return render (request, "base/registration.html", {"form":form})

def login_request(request):
	form = LoginForm()

	if request.method == "POST":
		form = LoginForm(request, data=request.POST)

		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("../")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")

	return render (request, "base/login.html", {"form":form})