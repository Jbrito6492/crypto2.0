from rest_framework import serializers
from crypto_api.models import Crypto


class CryptoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crypto
        fields = '__all__'
