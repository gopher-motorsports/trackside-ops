from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Test(models.Model):
    weather = models.CharField(max_length=100)
    temperature = models.IntegerField()
    driver = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    track = models.CharField(max_length=100, blank=True)
    fast_lap = models.CharField(max_length=100, blank=True)
    engine = models.CharField(max_length=100, blank=True)
    software = models.FloatField(blank=True)
    comments = models.TextField(blank=True)
    created_at = models.DateTimeField(default=now)

