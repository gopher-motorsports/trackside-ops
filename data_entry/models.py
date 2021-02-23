from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
from django.utils.timezone import now


class Person(models.Model):
    email = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    subteam = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, default=000-000-0000)
    licensed = models.BooleanField(default=False)

class Test(models.Model):
    weather = models.CharField(max_length=100)
    temperature = models.IntegerField()
    driver = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    track = models.CharField(max_length=100, blank=True)
    fast_lap = models.CharField(max_length=100, blank=True)
    tires = models.CharField(max_length=100)
    tire_condition = models.CharField(max_length=100)
    engine = models.CharField(max_length=100, blank=True)
    software = models.FloatField(blank=True)
    comments = models.TextField(blank=True)
    created_at = models.DateTimeField(default=now)
    personnel = ArrayField(models.CharField(max_length=200), null=True)
    