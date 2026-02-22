
def binary(num):
    if not num:
        return "0"
    bits = []
    q = num
    while q:
        r = 1 if (q & 1) else 0
        q = q >> 1
        bits = [r] + bits
    # print(bits)
    return "".join(map(lambda x: str(x), bits))


def count_set_bits(num):
    c = 0
    q = num
    while q:
        r = 1 if (q & 1) else 0
        c += r
        q = q >> 1
    return c
