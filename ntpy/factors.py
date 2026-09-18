from .primes import is_prime
def factorize(n):
    if n==1: return 1
    elif is_prime(n): return {n:1}
    else:
        results={}
        i=2
        p=0
        while n>1:
            if n%i==0:
                p=0
                results[i]=0
                while n%i==0:
                    results[i]+=1
                    n//=i
            else:p+=1
            if p==15:
                if is_prime(n):
                    results[n]=1
                    n=1
                else:
                    p=0
            i+=1
        return results
def prime_factorize(n):
    return list(factorize(n).keys())
def divisors(n):
    if is_prime(n): return [1,n]
    else: return [i for i in range(1,n+1) if n%i==0]
def num_divisors(n):
    return sum(1 for i in divisors(n))
def sum_divisors(n):
    return sum(divisors(n))
