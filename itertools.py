
"""iterations"""

import operator
from collections import Counter
from math import factorial
from functools import reduce

def npermutations(l):
    num = factorial(len(l))
    mults = Counter(l).values()
    den = reduce(operator.mul, (factorial(v) for v in mults), 1)
    return num / den

print(int(npermutations([2,3,8,9])))