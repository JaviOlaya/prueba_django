from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from main_app.forms import RegisterForm
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
        
        if request.method == 'POST':
            register_form = RegisterForm(request.POST)
            
            if register_form.is_valid():
                register_form.save()
                messages.success(request, 'Te has registrado correctamente')

                return redirect('index')
            else:
                messages.warning(request,"Datos usuario incorrectos")
    return render(request, 'users/register.html',{
        'title': 'registro',
        'register_form': register_form
    })
    
    
def login_page(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        #verificación:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('index')
                
            else:
                messages.warning(request,"Datos usuario incorrectos")
                
    return render(request, 'users/login.html',{
        'title': 'Login'
    })
def logout_page(request):
    logout(request)
    return redirect('login')
