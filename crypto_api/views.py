from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from crypto_api import serializers
from crypto_api.models import Crypto


class CryptoApiView(APIView):
    """Main CryptoApiView"""
    serializer_class = serializers.CryptoSerializer

    def get(self, request, format=None):
        """Returns a list of APIView Cryptos"""
        try:
            qs = Crypto.objects.all()
            serializer = self.serializer_class(qs, many=True)
            return Response(serializer.data)
        except Crypto.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        """Add Crypto information to db"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.create(request.data)
            return Response({'data': serializer.data})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
