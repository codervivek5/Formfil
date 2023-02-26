from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.loginpage, name='loginpage'),
    path('about', views.about, name='about'),
]