from adt.item import DPTCell
from adt.mat import Mat

''' lcs naive
    O(n^2) time, O(n) space
'''
def lcs_naive(s1, s2):
    m = len(s1)
    n = len(s2)

    lcs = ""
    j = 0
    for i in range(n):
        while(j < m and s1[j] != s2[i]):
            j += 1
        # chars match at i, j
        if j < m:
            # found
            lcs += s2[i]   # or larger[j]
        else:
            # not found, start over
            j = 0
        i += 1
    return lcs


def lcs(s1, s2):
    r = len(s1) + 1
    c = len(s2) + 1
    d0 = DPTCell(0, [])
    dpt = Mat(r, c, d0)
    # print(dpt)

    for i in range(1, r):
        for j in range(1, c):
            d = None
            if s1[i-1] == s2[j-1]:
                # add 1 to dpt[i-1][j-1], as another char is common in subsequence
                d = dpt.get(i-1, j-1).add(DPTCell(1, [s1[i-1]]))
            else:
                # set it to max(dpt[i][j-1]], dpt[i-1][j]), as this carries forward the max so far without either of the two chars one at a time (without both is already covered in a previous iter of i-i, j-1)
                # not using max() since we also capture the sequence
                if dpt.get(i, j-1).vl >= dpt.get(i-1, j).vl:
                    d = dpt.get(i, j-1)
                else:
                    d = dpt.get(i-1, j)
            dpt.set(i, j, d)
    return dpt

