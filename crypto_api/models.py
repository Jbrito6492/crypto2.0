from django.db import models


class Crypto(models.Model):
    """General crypto class"""
    ticker = models.CharField(max_length=25, unique=True)
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=250)
