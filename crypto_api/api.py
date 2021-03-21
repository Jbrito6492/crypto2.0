from crypto_api.models import Crypto
from rest_framework import viewsets, permissions
from .serializers import CryptoSerializer


class CryptoViewSet(viewsets.ModelViewSet):
    """ViewSet for main Crypto class"""
    queryset = Crypto.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CryptoSerializer
