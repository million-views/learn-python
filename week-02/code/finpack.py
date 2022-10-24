"""
FinPack: A collection of finance related classes and functions.
"""

import yfinance as yf
from datetime import date, timedelta


def avg(symbol, points=50, what='close'):
    """
    Compute the average price of a given stock `symbol`

    The number of data points to fetch is specified by `points` which
    defaults to 50, and the price to average is specified by `what`,
    which defaults to the `closing` price.

    todo:
    - discuss and refine the API for user convenience

    references:
      - https://aroussi.com/post/python-yahoo-finance
      - https://pandas.pydata.org/pandas-docs/stable/index.html
    """
    start = (date.today() - timedelta(days=points)).isoformat()
    end = (date.today() - timedelta(days=1)).isoformat()
    data = yf.download(symbol, start=start, end=end)
    mean = None
    if what == 'close':
        # study the documentation of `yfinance` and `pandas`
        # by following the links given under references above
        # and return the mean value. Note this is not the rolling
        # average which we will work on in the next class.
        # mean = 'your assignment work goes here!'
        mean = round(data['Close'].mean(), 2)
    elif what == 'open':
        # TODO: we'll fill the remaining options in next class
        # or if you want to get ahead, go for it.
        print('fix-me:', what)
    else:
        print('fix-me-too:', what)

    return mean