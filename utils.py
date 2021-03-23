import ccxt
limit = 10

print(ccxt.cex().fetch_ticker('BTC/USD'))
