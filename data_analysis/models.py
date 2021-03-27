from crypto_api.models import Crypto
from django.db import models


class Data(models.Model):
    crypto = models.ForeignKey(Crypto, on_delete=models.CASCADE)
    simple_return = models.FloatField(null=True)
    log_return = models.FloatField(null=True)
    beta = models.FloatField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{crypto}: simple return - {simple_return}, log return - {log_return}, beta - {beta}'
