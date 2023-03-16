from django.db import models
from asyncio.windows_events import NULL
from curses.ascii import NUL
from distutils.command.upload import upload
import email
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import AbstractUser

# Create your models here.

# class User(AbstractUser):
#     FirstName=models.TextField('FirstName',default='')
    # LastName=models.TextField('lname',default='',blank=True)
    
    
class User(AbstractUser):
     image=models.ImageField('image',upload_to='',null=True,blank=True)

class contactdetails(models.Model):
    name = models.TextField('name',max_length=200)
    country = models.CharField('country',max_length=200)
    email=models.EmailField('email',max_length=30,default='')
    contact=models.IntegerField('contact',default='')
    message=models.TextField('message',max_length=300,default='')

def __str__(self):
        return self.name