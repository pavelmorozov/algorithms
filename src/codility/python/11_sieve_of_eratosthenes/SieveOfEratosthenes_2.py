#17:21 - 17:41
def sieve(n):
    sieve = [True]*(n+1)
    sieve[0] = False
    sieve[1] = False
    i=2
    while i*i <= n:
        if sieve[i]==True:
            k = i*i
            while k <= n:
                sieve[k]=False
                k+=i
        i+=1
    return sieve

print(sieve(17))