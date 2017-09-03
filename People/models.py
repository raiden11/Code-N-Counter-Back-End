from django.db import models

from django.contrib.auth import settings


class Person(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)




