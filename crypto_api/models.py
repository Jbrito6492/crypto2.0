from django.db import models


class Crypto(models.Model):
    """General crypto class"""
    ticker = models.CharField(max_length=25, unique=True)
    current_price = models.FloatField(null=True)
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=250)

    def __str__(self):
        """Return string representation of Crypto"""
        return str(self.name)
