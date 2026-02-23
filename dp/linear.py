
''' fib: 
    linear solution for fibonacci
    it follows series from 0, 1, ..., because even though Fibonacci himself started it from 1, 2, ..., he was not the authority for this series which pre-dated him by thousands of years in Indian texts.
'''
def fib(n): 
    fa, fb = 0, 1
    if not n:
        return fa
    if n == 1:
        return fb
    for i in range(2, n+1):
        fa, fb = fb, fa + fb
    return fb


''' classic dp with memo, much less efficient than the linear one above, in both space and time
'''
def fib_memo(n, memo):
    if n in memo:
        # print("memo used for", n)
        return memo[n]
    if n == 0:
        memo[0] = 0
        return 0
    elif n == 1:
        memo[1] = 1
        return 1
    else:
        fn_1 = fib_memo(n-1, memo)
        fn_2 = fib_memo(n-2, memo)
        fn = fn_1 + fn_2
        memo[n] = fn
        return fn
