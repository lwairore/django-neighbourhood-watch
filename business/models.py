from django.db import models
from django.contrib.auth.models import User
from profile_user.models import Neighbourhood

# Create your models here.
class Business(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(default='No description has been given')
    user_id = models.ForeignKey(User)
    image = models.ImageField(upload_to='business/')
    neighbourhood_id = models.ForeignKey(Neighbourhood)
    email = models.EmailField()
    