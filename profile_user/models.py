from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Neighbourhood(models.Model):
    # name = models.CharField(max_length=30)
    location = models.CharField(max_length=30, default="No location")
    occupant_count = models.IntegerField()

    def create_neighbourhood(self):
        self.save()

    def delete_neighbourhood(self):
        self.delete()

    def find_neihbourhood():
        pass

    def __str__(self):
        return self.location
    
class Profile(models.Model):
    image = models.ImageField(upload_to='profile_image')
    bio = models.TextField()
    # name = models.CharField(max_length=40)
    user_id = models.ForeignKey(User)
    neighbourhood = models.ForeignKey(Neighbourhood, blank=True)
    location = models.CharField(max_length=30, default="Enter Location")


