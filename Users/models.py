from __future__ import unicode_literals

from django.db import models


class User(models.Model):

    PhoneNo = models.CharField(max_length=300,  unique=True)
    FirstName = models.CharField(max_length=300)
    LastName = models.CharField(max_length=300)
    Latitude = models.FloatField(blank=True, null=True)
    Longitude = models.FloatField(blank=True, null=True)
    DisplayURL = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):

        return self.FirstName + " " + self.LastName



