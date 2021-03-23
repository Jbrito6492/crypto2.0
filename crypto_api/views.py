from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from crypto_api import serializers


class CryptoApiView(APIView):
    """Main CryptoApiView"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        return Response({'message': 'hello'})
