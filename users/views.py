from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from .forms import LoginForm, UserRegistrationForm

def sign_in(request):
    if request.method == 'POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request, username=username, password=password)

            if user is not None and user.is_active:
                login(request, user)
                messages.success(request,'Login request was successfull')
                return redirect('market:home')
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('users:login')
    else:
        form=LoginForm()
    return render(request, 'users/login.html',{'form':form})

def sign_out(request):
    logout(request)
    messages.success(request,'Logout request was successfull')
    return redirect('users:login')

def sign_up(request):
    if request.method == 'POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            return render(request,'users/register_done.html',{'user':user})
        
    else:
        form=UserRegistrationForm()
    return render(request,'users/register.html',{'form':form})
