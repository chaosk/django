"""
Testing of admin inline formsets.
"""
import random

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Holder5(models.Model):
    dummy = models.IntegerField()


class Inner5(models.Model):
    dummy = models.IntegerField()
    holder = models.ForeignKey(Holder5, models.CASCADE)

