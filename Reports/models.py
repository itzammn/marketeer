from django.db import models
from django.contrib.auth.models import User

class Report(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Feedback(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    message = models.TextField(help_text="enter ur feedback")

    def __str__(self):
        return self.user
