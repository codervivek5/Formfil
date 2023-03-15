from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash 
from django.contrib import messages 
from home.models import contactdetails
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
# Create your views here.

def index(request):
    # return HttpResponse("this is home page")
    return render(request, "index.html")

def loginpage(request):
    # return HttpResponse("this is home page")
    return render(request, "login.html")

def userdashboard(request):
    if request.user.is_authenticated:
       return render(request,"user_dashboard.html")
    messages.info(request,"Please login first")
    return redirect('loginpage')

def logout1(request):
    logout(request)
    messages.info(request,'Successfully logged out!')
    return redirect('loginpage')

def loginemail(request):
    if request.method=="POST":
        email    = request.POST['email']
        password :str    =  request.POST['password']
        
        username = User.objects.get(email=email.lower()).username
        user = authenticate(username=username, password=password)
        if user is not None:
            print("correct")
            login(request,user)
            return render(request,"user_dashboard.html")

    return render(request, "loginemail.html")

User = get_user_model()
def signup(request):
    if request.method=="POST":
        fname :str    =  request.POST['fname']
        lname :str    =  request.POST['lname']
        email    = request.POST['email']
        password :str    =  request.POST['password']
        cnfpassword :str    =  request.POST['cnfpassword']

        if password != cnfpassword:
                messages.info(request, ' Sorry! Password does not match')
                return redirect('/signup/')

        if User.objects.filter(email=email).exists():
                    messages.info(request, ' Sorry! Email is already registered')
                    print("sorry")
                    return redirect('/signup/')
        if User.objects.filter(username=fname+lname).exists():
                    messages.info(request, ' Sorry! Username is already registered')
                    print("sorry")
                    return redirect('/signup/')
        
        myuser = User.objects.create_user(fname+lname, email,password,first_name=fname, last_name=lname)
        myuser.save
        messages.info(request, ' Successfully registered! ')
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

