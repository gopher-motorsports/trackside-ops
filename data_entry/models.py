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
	is_deleted = models.BooleanField(default=False)
	flagged = models.BooleanField(default=False)
	date = models.CharField(max_length=50)
	time = models.CharField(max_length=50)
	chassis = models.CharField(max_length=10)
	car = models.CharField(max_length=50)
	driver = models.CharField(max_length=100)
	motor = models.CharField(max_length=100, blank=True)
	motor_comments = models.CharField(max_length=100, blank=True)
	location = models.CharField(max_length=100)
	drive_day_lead = models.CharField(max_length=100)
	track = models.CharField(max_length=100, blank=True)
	weather = models.CharField(max_length=100)
	air_temp = models.IntegerField()
	track_temp = models.IntegerField()
	temperature_unit = models.CharField(max_length=5)
	wind_direction = models.CharField(max_length=10)
	wind_speed = models.IntegerField()
	tires = models.CharField(max_length=100)
	fl_tire_serial_number = models.CharField(max_length=100)
	fl_tire_condition = models.CharField(max_length=100)
	fr_tire_serial_number = models.CharField(max_length=100)
	fr_tire_condition = models.CharField(max_length=100)
	bl_tire_serial_number = models.CharField(max_length=100)
	bl_tire_condition = models.CharField(max_length=100)
	br_tire_serial_number = models.CharField(max_length=100)
	br_tire_condition = models.CharField(max_length=100)
	data_file_link = models.CharField(max_length=100)
	comments = models.TextField(blank=True)
	image = models.FileField()
	image_data = models.BinaryField()
	created_at = models.DateTimeField(default=now)
