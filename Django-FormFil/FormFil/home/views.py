from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse("this is home page")
    return render(request, "index.html")

    
def about(request):
    return HttpResponse("this is about page")
def login(request):
    return render(request,"login.html")
def signup(request):
    return render(request,"signup.html")

def contact_us(request):
    return render(request,"contact-us.html")
def about_us(request):
    return render(request,"about_us.html")