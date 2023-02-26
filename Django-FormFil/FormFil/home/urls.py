from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.loginpage, name='loginpage'),
    path('signup/', views.signup, name='signup'),
    path('about/', views.about, name='about'),
    path('cart/', views.cart, name='cart'),
    path('contact/', views.contactus, name='contactus'),
    path('service/', views.service, name='service'),
]