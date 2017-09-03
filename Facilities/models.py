from __future__ import unicode_literals

from django.db import models


class Facility(models.Model):

    Category = models.CharField(max_length=300, blank=True, null=True)
    CKey = models.IntegerField(blank=True)
    Title = models.CharField(max_length=300, blank=True, null=True)
    ImageURL = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.Category + " - " + self.Title

