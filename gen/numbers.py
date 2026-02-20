import math
MIRROR_DIGITS = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}

def mirrored(digit):
    return MIRROR_DIGITS.get(digit, -1)

def digits(num):
    ds = []
    if not num:
        ds.append(0)
        return ds
    while num >= 1:
        r = num % 10
        ds.append(r)
        num = int(num/10)
    return list(reversed(ds))

def number(digits):
    ds = list(reversed(digits))
    ten_power = 0
    num = 0
    for d in ds:
        num += d * (10 ** ten_power)
        ten_power += 1
    return num

def is_mirrored_all(digits):
    for d in digits:
        if mirrored(d) == -1:
            # digit cannot be mirrored
            return False
    return True

def mirror_all(digits):
    md = []
    for d in digits:
        if mirrored(d) >= 0: # redundant if used with is_mirrored_all first
            md.append(mirrored(d))
    return md


''' confusing numbers
    find valid numbers obtained by rotating digits by 180 - only these digits can be rotated - 0,1,6,8,9
'''
def confusing_naive(num):
    # check all numbers if they can be rotated
    res = {}
    for n in range(num+1):
        if n in res:
            continue
        ds = digits(n)
        if is_mirrored_all(ds):
            res[n] = True
            ds_mrr = mirror_all(ds)
            m = number(ds_mrr)
            if m < num + 1:
                # only add ones less than given N
                res[m] = True
    return list(sorted(res.keys()))


def combine_digits(pwr10, n, ds, limit=0):
    cmb = []
    if not ds:
        pwr10 = 0
        ds = [0]
    for d in ds:
        num = n * 10 ** pwr10 + d
        if (limit and num <= limit) or not limit:
            cmb.append(num)
    return cmb


def cross_combine(xs, ys, limit=0):
    if not xs:
        return ys, 0
    if not ys:
        return xs, 0
    xyc = []
    l10 = math.log10(ys[-1])
    pwr10x = int(l10) + 1
    last = 0
    for x in xs:
        for y in ys:
            n = x * (10 ** pwr10x) + y
            if limit and n > limit:
                if not last:
                    # capturing last helps with looping up to limit in caller, since the loop may not end at limit
                    last = n
                break
            xyc.append(n)
    return xyc, last

''' OPT: calculate mirrored list of 1 digit, then add them as prefix digit each and repeat first list to get mirrored list of 2 digits, then add 3rd digit as prefix and add all so far for 2 digits to make 3 digit list, etc.
'''
def confusing(limit):
    xs = list(MIRROR_DIGITS.keys())
    lm = len(xs)
    curr = -1
    ys = []
    i = 0
    while curr <= limit:
        ys, last = cross_combine(xs, ys, limit)
        # print(i, ys)
        i += 1
        if not ys:
            break
        curr = max(ys[-1], last)

    return ys
