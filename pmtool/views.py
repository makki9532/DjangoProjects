from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome, {username}!")
            return redirect('home')  # Redirect to the same page or another as needed
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

from django.contrib.auth.models import User

def registerUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        else:
            User.objects.create_user(username=username, password=password)
            messages.success(request, "Account created successfully. Please log in.")
            return redirect('login')
    return render(request, 'register.html')

def home(request):
    return render(request, 'home.html')

from django.contrib.auth import logout

def logoutUser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')