
from adt.item import *
from adt.mat import Mat

''' 01 knapsack problem
    canonical dp algorithm

    for every i, j in dp table, select max val of
    1. adding item i -> val(i) + val(i-1, rest)
    2. not adding item i -> val(i-1, j)

    e.g. dp table 
    target: 10
    items:
    2   1   5   3
    val:
    3   2   4   5

    w       0   1   2   3   4   5   6   7   8   9   10
    i       0   0   0   0   0   0   0   0   0   0   0
    2       0   0   3   3   3   3   3   3   3   3   3
    1       0   2   3   5   5   5   5   5   5   5   5
    5       0   2   3   5   5   5   6   7   9   9   9
    3       0   2   3   5   7   8   10  10  10  11  12
'''

def knap(items, target):
    r, c = len(items) + 1, target + 1
    d0 = DPTCell(0, [])
    dpt = Mat(r, c, d0)
    for i in range(1, r):
        item = items[i-1]
        for j in range(1, c):
            # case 1: add i if it can fit
            if item.wt <= j:
                rem = j - item.wt
                d_rem = dpt.get(i-1, rem)
                d_i = DPTCell(item.vl, [item]).add(d_rem)
            else:
                d_i = d0   # DPTCell(0, [])
            # case 2: don't add i
            d_not_i = dpt.get(i-1, j)
            # select the case with more value
            if d_i.vl > d_not_i.vl:
                d_ij = d_i
            else:
                d_ij = d_not_i
            dpt.set(i, j, d_ij)
    # print(dpt)
    return dpt.get(r-1, c-1)
