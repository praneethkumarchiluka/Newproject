from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User,auth

def register(request):
    

    if request.method=='POST':
        print('this is post')
        fname=request.POST['first_name']
        password1=request.POST['password1']
        
        
        user=User.objects.create_user(username=fname,password=password1)
        user.save()
        return redirect('users:login')


    return render(request,'Registration/register.html')

def loginfn(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user= authenticate(request, username=username, password=password)
        
        if user is not None:
            print('not none')
            login(request, user)
            return redirect('test1:show')
        else:
            messages.info(request,'Username or Password is incorrect')
    return render(request,'Registration/login.html')

def logoutUser(request):
    logout(request)
    return redirect('users:login')