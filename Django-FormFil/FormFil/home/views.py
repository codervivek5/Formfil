from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash 
from django.contrib import messages 
from home.models import contactdetails
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
    if request.method=="POST":
        name :str    =  request.POST['fname']
        email    = request.POST['email']
        contact =  request.POST['contact']
        country  :str=  request.POST['country']
        message  :str=  request.POST['subject']

        cdata=contactdetails()
        cdata.name=name
        cdata.email=email
        cdata.contact=contact
        cdata.message=message
        cdata.country=country
        cdata.save()
        print('SUCCESS')
    return render(request, "contact-us.html")

def cart(request):
    # return HttpResponse("this is home page")
    return render(request, "cart.html")

def service(request):
    return render(request, "service.html")

def about(request):
    return render(request, "about_us.html")

