from django.shortcuts import render,redirect

def show(request):    
    return render(request,"home.html")  
