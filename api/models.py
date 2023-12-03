# artists/models.py

from django.db import models
from django.contrib.auth.models import User

class Work(models.Model):
    LINK_CHOICES = [
        ('YT', 'Youtube'),
        ('IG', 'Instagram'),
        ('Other', 'Other'),
    ]

    link = models.URLField()
    work_type = models.CharField(max_length=10, choices=LINK_CHOICES)

class Artist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    works = models.ManyToManyField(Work)
