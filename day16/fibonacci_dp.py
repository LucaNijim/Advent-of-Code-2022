import time


def memoize(k):
    previously_tried_vals = {}

    def helper_func(n):
        if n not in previously_tried_vals:
            previously_tried_vals[n] = k(n)
        return previously_tried_vals[n]

    return helper_func


@memoize
def fib(n):
    if n<2:
        return n
    return fib(n-2)+fib(n-1)

start = time.time()
print(fib(32))
print('Time elapsed: '+str(time.time()-start))