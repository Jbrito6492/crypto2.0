from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


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
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Crypto.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        """Add Crypto information to db"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(request.data)
            return Response({'data': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def patch(self, request, pk, format=None):
        """Update Crypto instance in DB"""
        crypto_coin = Crypto.objects.get(id=pk)
        serializer = self.serializer_class(
            crypto_coin, data=request.data)
        if serializer.is_valid():
            return Response({'data': serializer.data}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, pk):
        """Delete Crypto instance in DB"""
        try:
            crypto_coin = Crypto.objects.get(id=pk)
            crypto_coin.delete()
            return Response({'data': 'crypto deleted successfully'}, status=status.HTTP_202_ACCEPTED)
        except Crypto.DoesNotExist:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
