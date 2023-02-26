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

def about(request):
    return HttpResponse("this is about page")

