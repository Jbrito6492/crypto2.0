from rest_framework import serializers
from crypto_api.models import Crypto


class CryptoSerializer(serializers.ModelSerializer):
    """Serializes fields from Crypto model"""
    class Meta:
        model = Crypto
        fields = '__all__'
