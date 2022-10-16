# A driver to test functions from our very own `finpack` module

import finpack

stock = input('type a stock symbol: ')
try:
    print('the average of 50 days closing price is: ', finpack.avg(stock))
except:
    print('Oops!')
