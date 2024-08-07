from django.db import models
from devices.models import Device


class Location(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.BigIntegerField()
