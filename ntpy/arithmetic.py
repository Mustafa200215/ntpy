from math import prod
from .factors import prime_factorize , factorize
def euler_phi(n):
    if n==1:return 1
    else:
        prime=prime_factorize(n)
        for p in prime:
            n-=n//p
        return n
def mobius(n):
    f=factorize(n)
    if n==1:return 1
    elif all(i==1 for i in f.values()): return (-1)**len(f)
    else:return 0
