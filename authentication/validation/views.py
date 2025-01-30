from django.shortcuts import render,redirect
from .forms import UserRegistration, Loginform
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required 


def home(request):
    return render(request, 'main.html')


def register(request):
    form  = UserRegistration()
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():

            form.save()

            return redirect('login')
        
    context = {'form': form}
    return render(request, 'register.html',context)


def login(request):
    form = Loginform()

    if request.method == 'POST':
        form = Loginform(request, data=request.POST)
        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request,username=username, password=password)

            if user is not None:

                auth.login(request,user)

                return redirect('dashboard')
    
    context = {'loginform':form}
    
    return render(request, 'login.html', context)


@login_required(login_url= 'login')
def dashboard(request):
    return render(request, 'dashboard.html')



def user_logout(request):
    auth.logout(request)

    return redirect('home')
