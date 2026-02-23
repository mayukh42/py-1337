
def fib(n): 
    fa, fb = 0, 1
    if not n:
        return fa
    if n == 1:
        return fb
    for i in range(2, n+1):
        fa, fb = fb, fa + fb
    return fb
