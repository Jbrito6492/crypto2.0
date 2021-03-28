from crypto_api.models import Crypto

from data_analysis.models import Data
from data_analysis.serializers import DataSerializer
import datetime

import numpy as np
import pandas as pd
from pandas_datareader import data as wb

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class DataViewApi(APIView):
    """A ViewSet for data analysis"""
    serializer_class = DataSerializer

    tod = datetime.datetime.now()
    d = datetime.timedelta(days=365)
    five_years = datetime.timedelta(days=1825)
    a = tod - d
    b = tod - five_years

    def get(self, request, pk=None, format=None):
        """Return Data about Crypto Id"""
        t_return = {}
        try:
            qs = Crypto.objects.filter(id=pk)
            ticker = ''.join([x.ticker for x in qs])
            Ticker = wb.DataReader(
                ticker, data_source="yahoo", start=self.a)["Adj Close"]

            """Logic for daily simple return"""
            Ticker["simple_return"] = (
                Ticker / Ticker.shift(1)) - 1
            avg_returns_d = Ticker["simple_return"].mean()
            t_return['simple_return'] = "{s_return:.5f}%".format(
                s_return=avg_returns_d * 100)

            """Logic for beta calculation"""
            tickers = [ticker, '^CMC200']
            data = pd.DataFrame()
            for t in tickers:
                data[t] = wb.DataReader(t, data_source='yahoo', start=self.b)[
                    'Adj Close']
            sec_returns = np.log(data / data.shift(1))
            cov = sec_returns.cov() * 365
            cov_with_market = cov.iloc[0, 1]
            market_var = sec_returns['^CMC200'].var() * 365
            t_beta = cov_with_market / market_var
            t_return['beta'] = "%.5f" % t_beta

            return Response(t_return, status=status.HTTP_200_OK)
        except Data.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
