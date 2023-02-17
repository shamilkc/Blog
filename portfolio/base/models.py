
from django.db import models

# Create your models here.


class Con(models.Model):
    name =models.CharField(max_length=25)
    email =models.CharField(max_length=30)
    subject = models.CharField(max_length=35)
    messege = models.TextField()


class Pro(models.Model):
    name = models.CharField(max_length=35)
    description =models.CharField(max_length=50)
    link = models.CharField(max_length=255)
