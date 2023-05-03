from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    city = models.CharField(max_length=30, blank=True)
    dob = models.DateField(null=True, blank=True)
    pic = models.ImageField(upload_to='profile/pics', null=True, blank=True)

    def __str__(self):
        return self.user.username
