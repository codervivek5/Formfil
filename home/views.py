from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse("this is home page")
    return render(request, "index.html")

    
def about(request):
    return HttpResponse("this is about page")


