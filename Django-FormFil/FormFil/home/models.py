from django.db import models
from asyncio.windows_events import NULL
from curses.ascii import NUL
from distutils.command.upload import upload
import email
from email.policy import default
from unittest.util import _MAX_LENGTH
# Create your models here.

class contactdetails(models.Model):
    name = models.TextField('name',max_length=200)
    country = models.CharField('country',max_length=200)
    email=models.EmailField('email',max_length=30,default='')
    contact=models.IntegerField('contact',default='')
    message=models.TextField('message',max_length=300,default='')

def __str__(self):
        return self.name