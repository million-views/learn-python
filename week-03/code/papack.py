"""
PaPack: contains super helpful and fast predictive analytics functions

A pretend module that exists to illustrate code organization and to
isolate class assignment instructions in one place.
"""
from efficient_apriori import apriori

def analyze(transactions, min_support=0.5, min_confidence=1, uselib=True):
    if uselib is True:
      itemsets, rules = apriori(transactions, min_support, min_confidence)
      return (itemsets, rules)
    else:
      return ("I am ", "trying")
