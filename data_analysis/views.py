from crypto_api.models import Crypto

from data_analysis.models import Data
from data_analysis.serializers import DataSerializer
import datetime

from pandas_datareader import data as wb

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class DataViewApi(APIView):
    """A ViewSet for data analysis"""
    serializer_class = DataSerializer

    tod = datetime.datetime.now()
    d = datetime.timedelta(days=365)
    a = tod - d

    def get(self, request, pk=None, format=None):
        """Return Data about Crypto Id"""
        t_return = {}
        try:
            qs = Crypto.objects.filter(id=pk)
            ticker = ''.join([x.ticker for x in qs])
            Ticker = wb.DataReader(
                ticker, data_source="yahoo", start=self.a)
            Ticker["simple_return"] = (
                Ticker["Adj Close"] / Ticker["Adj Close"].shift(1)) - 1
            avg_returns_d = Ticker["simple_return"].mean()
            t_return[ticker] = "{s_return:.5f}%".format(
                s_return=avg_returns_d * 100)
            return Response(t_return, status=status.HTTP_200_OK)
        except Data.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
