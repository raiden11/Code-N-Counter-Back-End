from __future__ import unicode_literals

from django.db import models


class Complaint(models.Model):

    Subject = models.CharField(max_length=100, blank=True, null=True)
    Body = models.TextField(blank=True, null=True)
    Status = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):

        return str(id)

    def save(self, *args, **kwargs):

        if self.Subject[0] == 'C':
       
            self.Status = "Your Complaint has been lodged. Necessary action will be taken within 24 hours."
        else:
            self.Status = "Your Complaint has been lodged. Necessary action will be taken within 1 hour."

        super(Complaint, self).save(*args, **kwargs)

