from __future__ import unicode_literals

from django.db import models
from Facilities.models import Facility


class Store(models.Model):

    ParKey = models.ForeignKey(Facility, blank=True, null=True)
    Name = models.CharField(max_length=300, blank=True, null=True)
    Latitude = models.FloatField(blank=True, null=True)
    Longitude = models.FloatField(blank=True, null=True)
    LinkURL = models.CharField(max_length=300, blank=True, null=True)
    PhoneNo = models.CharField(max_length=300, blank=True, null=True)
    Address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.Name




