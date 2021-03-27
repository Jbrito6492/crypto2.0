from data_analysis.serializers import DataSerializer

from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from data_analysis.models import Data


class DataViewSet(ViewSet):
    """A ViewSet for data analysis"""
    serializer_class = DataSerializer

    def retrieve(self, request, pk):
        """Return Data about Crypto Id"""
        try:
            qs = Data.objects.filter(crypto=pk)
            serializer = self.serializer_class(qs, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Data.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
