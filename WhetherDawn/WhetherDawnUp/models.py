from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=100)
    coord_B = models.CharField(max_length=10)
    coord_L = models.CharField(max_length=10)
    coord_H = models.FloatField()

    def __str__(self):
        return self.name