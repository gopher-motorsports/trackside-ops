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


class Drives(models.Model):
    motor_num = models.CharField(max_length=100)
    car_type = models.CharField(max_length=10)
    is_racespec = models.BooleanField(default=False)
    weather = models.CharField(max_length=100)
    temperature = models.IntegerField()
    air_temp = models.IntegerField()
    track_temp = models.IntegerField()
    driver = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    track = models.CharField(max_length=100, blank=True)
    is_dyno = models.BooleanField(default=False)
    tires = models.CharField(max_length=100)
    tire_condition = models.CharField(max_length=100)
    engine = models.CharField(max_length=100, blank=True)
    comments = models.TextField(blank=True)
    created_at = models.DateTimeField(default=now)
    drive_day_lead = models.CharField(max_length=100)
