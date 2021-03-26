from crypto_api.models import Crypto
from django.db import models


class Data(models.Model):
    crypto = models.ForeignKey(Crypto, null=True, on_delete=models.CASCADE)
    simple_return = models.FloatField(null=True)
    log_return = models.FloatField(null=True)
    beta = models.FloatField(null=True)
