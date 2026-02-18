
def mirrored(digit):
    mirror = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
    return mirror.get(digit, -1)

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

