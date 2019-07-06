from django.db import models
from django.contrib.auth.models import User
from profile_user.models import Profile

# Create your models here.
class Business(models.Model):
    name = models.CharField(max_length=30)
    user_id = models.ForeignKey(User)
    neighbourhood_id = models.ForeignKey(Profile)
    email = models.EmailField()
    