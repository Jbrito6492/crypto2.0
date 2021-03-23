from rest_framework import serializers
from crypto_api.models import Crypto


class CryptoSerializer(serializers.Serializer):
    """Serializes fields from Crypto model"""
    ticker = serializers.CharField(max_length=25)
    name = serializers.CharField(max_length=25)
    current_price = serializers.FloatField(max_value=None, min_value=None)
    description = serializers.CharField(max_length=250)

    def create(self, validated_data):
        """Create new Crypto instance"""
        return Crypto.objects.create(**validated_data)
