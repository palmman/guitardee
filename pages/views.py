from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .models import Team

# Create your views here.

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    teams = Team.objects.all()
    data = {
        'teams' : teams
    }
    return render(request, 'pages/about.html', data)

def contact(request):
    return render(request, 'pages/contact.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('home')
        else:
            messages.error(request, 'Your Username or Password is incorrect')
            return redirect('login')
    return render(request,'pages/login.html')

def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists!')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists!')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email, username=username, password=password)
                    auth.login(request, user)
                    messages.success(request, 'You are now logged in.')
                    return redirect('home')
                    user.save()
                    messages.success(request, 'Registered successfully')
                    return redirect('login')

        else:
            messages.error(request, 'Password donot match')
            return redirect('register')
    else:
        return render(request,'pages/register.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are successfully logout.')
        return redirect('home')
    return redirect('home')
