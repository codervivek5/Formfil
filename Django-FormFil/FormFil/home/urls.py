from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('contactus',views.contact_us,name='contactus'),
    path('aboutus',views.about_us,name='aboutus'),
   
]