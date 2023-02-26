from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash 
from django.contrib import messages 
# Create your views here.

def index(request):
    # return HttpResponse("this is home page")
    return render(request, "index.html")

def loginpage(request):
    # return HttpResponse("this is home page")
    return render(request, "login.html")
def signup(request):
    # return HttpResponse("this is home page")
    return render(request, "signup.html")

def contactus(request):
    # return HttpResponse("this is home page")
    return render(request, "contact-us.html")

def cart(request):
    # return HttpResponse("this is home page")
    return render(request, "cart.html")

def service(request):
    return render(request, "service.html")

def about(request):
    return render(request, "about_us.html")

