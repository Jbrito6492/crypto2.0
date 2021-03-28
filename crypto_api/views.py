from crypto_api.models import Crypto
from crypto_api.serializers import CryptoSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class CryptoApiView(APIView):
    """Main CryptoApiView"""
    serializer_class = CryptoSerializer

    def get(self, request, pk=None, format=None):
        """Returns a list of APIView Cryptos"""
        try:
            if pk is not None:
                qs = Crypto.objects.get(id=pk)
                serializer = self.serializer_class(qs)
            else:
                qs = Crypto.objects.all()
                serializer = self.serializer_class(qs, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Crypto.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        """Add Crypto information to db"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def patch(self, request, pk, format=None):
        """Update Crypto instance in DB"""
        qs = Crypto.objects.get(id=pk)
        serializer = self.serializer_class(
            qs, data=request.data)
        if serializer.is_valid():
            return Response({'data': serializer.data}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, pk, format=None):
        """Delete Crypto instance in DB"""
        try:
            qs = Crypto.objects.get(id=pk)
            qs.delete()
            return Response({'data': 'crypto deleted successfully'}, status=status.HTTP_202_ACCEPTED)
        except Crypto.DoesNotExist:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
