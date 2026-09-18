from math import gcd
def crt(M,A):
    def solve(n,m,k,h):
        GCD=gcd(n,m)
        diff=h-k
        if GCD==1:
            inv=pow(n,-1,m)
            rem=(inv*diff)%m
            return n*m,n*rem+k
        else:
            if diff%GCD==0:
                inv=pow(n//GCD,-1,m//GCD)
                rem=(inv*(diff//GCD))%(m//GCD)
                return n*(m//GCD),n*rem+k
            else:
                return 0,0
    a=M[0]
    b=A[0]
    for i in range(1,len(M)):
        a,b=solve(M[i],a,A[i],b)
        if a==0:
            break
    return a,b
