from django.db import models

# Create your models here.
class Events(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='events/')
    posted_at = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=30)