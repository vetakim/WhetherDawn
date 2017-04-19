from django.db import models
from django.utils import timezone

# Create your models here.


class Coords(models.Model):
    coord_B = models.FloatField()
    coord_L = models.FloatField()
    coord_H = models.FloatField()
    created_date = models.DateTimeField(default=timezone.now)


class Sun(models.Model):
    time_rise = models.TimeField()
    time_set = models.TimeField()