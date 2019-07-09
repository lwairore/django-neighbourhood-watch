from django.db import models

# Create your models here.

class Contact(models.Model):
    title = models.CharField(max_length=30)
    number = models.CharField(max_length=12)
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=50, default="Enter Location")