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
min_support = 0.15
min_confidence = 0.5

#      a  b  c d e f
# I => 🍎 🍺 🍚 🍗 🍐 🍼
emoji_t1_set = [
    ('🍎', '🍺', '🍚', '🍗'),  # tx 1
    ('🍎', '🍺', '🍚'),        # tx 2
    ('🍎', '🍺'),              # tx 3
    ('🍎', '🍐'),              # tx 4
    ('🍼', '🍺', '🍚', '🍗'),   # tx 5
    ('🍼', '🍺', '🍚'),       # tx 6
    ('🍼', '🍺'),             # tx 7
    ('🍼', '🍐'),             # tx 8
]

#      a  b  c d  e
# I => 🥚 🥓 🍲 🍎 🍌
emoji_t2_set = [
    ('🥚', '🥓', '🍲'),  # eggs, bacon, soup
    ('🥚', '🥓', '🍎'),  # eggs, bacon, apple
    ('🍲', '🥓', '🍌')  # soup, bacon, banana
]
# [{eggs} -> {bacon}, {soup} -> {bacon}] @ min_support=0.5, min_confidence=1

#      a  b  c d  e  f
# I => 🍞 🥛 👶 🍺 🥚 🥤
emoji_t3_set = [
  ('🍞', '🥛'),              # tx 1
  ('🍞', '👶', '🍺', '🥚'),   # tx 2
  ('🥛', '👶', '🍺', '🥤'),   # tx 3
  ('🍞', '🥛', '👶', '🍺'),   # tx 4
  ('🍞', '🥛', '👶', '🥤'),   # tx 5
]

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
    # transactions = emoji_t2_set
    itemsets, rules = papack.analyze(transactions, min_support, min_confidence,
                                     True)
    # print(itemsets, rules)
    # print(rules)
    for rule in rules:
      print(rule)

except Exception as e:
    print('Oops!', e)
    # raise e
