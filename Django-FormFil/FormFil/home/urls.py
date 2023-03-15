from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.loginpage, name='loginpage'),
    path('loginemail/', views.loginemail, name='loginemail'),
    path('signup/', views.signup, name='signup'),
    path('about/', views.about, name='about'),
    path('cart/', views.cart, name='cart'),
    path('contact/', views.contactus, name='contactus'),
    path('service/', views.service, name='service'),
    path('userdashboard/', views.userdashboard, name='userdashboard'),
    path('logout1/', views.logout1, name='logout1'),
]