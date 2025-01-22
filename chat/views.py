from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import Message  # Ensure your Message model is defined properly
from django.db import models


def home(request):
    return render(request, 'chat/home.html')  # Create a template 'home.html'

# Login view
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to homepage after login
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'chat/login.html', {'form': form})

# Registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')  # Redirect to login page after registration
    else:
        form = UserCreationForm()
    return render(request, 'chat/register.html', {'form': form})

def room(request, room_name):
    try:
        # Fetch messages associated with the room_name
        messages = Message.objects.filter(room_name=room_name)
    except Exception as e:
        messages.error(request, f"Error fetching messages: {e}")
        messages = []

    return render(request, 'chat/room.html', {'room_name': room_name, 'messages': messages})



# Logout view
def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout
