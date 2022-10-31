# A driver to test functions from our very own `papack` module
"""
Setup:
- `cd` to `week-03/code` folder
- ensure `transactions.csv` is at the same location where this file
  (`main.py`) is.
- install requirements:
  `pip install -r requirements.txt`
- execute the script:
  `python main.py`
"""

import os
import csv
import papack

dbfilename = os.path.dirname(os.path.abspath(__file__)) + '/transactions.csv'

# min_support and min_confidence are extremely sensitive to the dataset
# read the `association rule mining` reference for further steps
# required after `apriori` does its thing...
#
# the objective of this assignment is to get you comfortable in using
# lists, tuples, sets and dicts while studying a useful application...
# so don't worry if the results are not `magical`
min_support = 0.1
min_confidence = 0.5
try:
    transactions = []
    with open(dbfilename) as db:
        tlist = csv.reader(db, delimiter=',')
        for row in tlist:
            # convert list to a tuple and add to transactions
            # limit items to the first 10 in the basket per entry
            # for this exercise
            basket = tuple(row[:10])
            transactions.append(basket)
            # print(len(basket), basket)

    # call the `analyze` function that does `apriori` on `transactions`
    itemsets, rules = papack.analyze(
        transactions,
        min_support,
        min_confidence,
    )
    print(itemsets, rules)
except Exception as e:
    print('Oops!', e)
