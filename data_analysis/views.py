from data_analysis import serializers

from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response


class DataViewSet(ViewSet):
    """An APIView for data analysis"""

    def list(self, request, pk):
        """Return Data about Crypto Id"""
