import random
from math import log2
def generate_primes(end):
    list_generate=[0,0]+[i for i in range(2,end+1)]
    for p in range(2,int(end**.5)+1):
        if list_generate[p]:
            for k in range(p*p,end+1,p):
                list_generate[k]=0
    return list(sorted(set(list_generate)))[1:]

def is_prime(n,k=20):
    if n in (2,3,5,7,11,13,17,19,23):return True
    elif n<23 or n%2==0:return False
    else:
        bases=random.sample(range(2,n-2),min(k,n-3))
        m=n-1
        s=int(log2(m&(-m)))
        d=m//(2**s)
        test=[]
        test_first=0
        for a in bases:
            x=pow(a,d,n)
            test+=[x]
            if x==1 or x==m:
                test_first+=1
        if test_first==len(bases):
            return True
        else:
            results=[]
            for x in test:
                if x!=1 and x!=m:
                    for _ in range(s):
                        x=pow(x,2,n)
                        if x==m:
                            results+=[True]
                            break
                    else:
                        results+=[False]
                else:
                    results+=[True]
            if all(results)==True:
                return True
            else:
                return False
