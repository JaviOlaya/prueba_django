from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from Mainapp.forms import RegisterForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    
    return render(request, 'main_app/index.html',{
        'title': 'Inicio'
    })
def register_page(request):
    if request.user.is_authenticated:
        return redirect('inicio')
    else: 
        register_form = RegisterForm()
        
    return render(request, 'users/register.html',{
        'title': 'registro'
    })
def login_page(request):
    
    return render(request, 'users/login.html',{
        'title': 'Login'
    })
def logout_page(request):
    
    return render(request, 'users/logout.html',{
        'title': 'Logout'
    })
