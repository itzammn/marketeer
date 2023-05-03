from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


class Campaign(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    target_audience = models.TextField()
    platform = models.CharField(max_length=255)
    status = models.CharField(max_length=20, default='draft')
    image = models.ImageField(upload_to='campaign_images', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    client = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Campaign, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Lead(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=255)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['email', 'campaign']

    def __str__(self):
        return self.email


