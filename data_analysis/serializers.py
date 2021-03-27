from rest_framework import serializers
from data_analysis.models import Data


class DataSerializer(serializers.ModelSerializer):
    """Serializes fields from Data model"""

    class Meta:
        model = Data
        fields = '__all__'
