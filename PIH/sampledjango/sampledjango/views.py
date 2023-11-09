from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate,login

def aboutus(request): #ABOUT-US
    return render(request,"aboutus.html")

def loginpage(request): #LOGIN PAGE
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if (user==None):
            print("user",user)

            return render(request,"login.html")
        else:
            login(request, user)
            return render(request, "index.html")
    return render(request,"login.html")

def Registration(request): #REGISTRATION
    return render(request,"Registration.html")

def Home(request): #HOME
    return render(request,"homepage.html")

