from django.db import models
from django.utils import timezone
from datetime import date

# Create your models here.


class Coords(models.Model):
    coord_B = models.CharField(max_length=10, default='55°45′07″')
    coord_L = models.CharField(max_length=10, default='37°36′56″')
    coord_H = models.FloatField(default=144)
    date = models.DateField(default=date.today)
    created_date = models.DateTimeField(default=timezone.now)


class Sun(models.Model):
    time_rise = models.TimeField()
    time_set = models.TimeField()