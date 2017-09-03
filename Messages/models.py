from __future__ import unicode_literals

from django.db import models
from Users.models import User


class Message(models.Model):

    Rec = models.ForeignKey(User, blank=True, null=True)
    msg = models.TextField(blank=True, null=True)

    def __str__(self):

        return str(id)


