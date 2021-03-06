#22:06 - 22:11
def getPrimes(n):
    primes = [0]*(n+1)
    i=2
    while i*i <= n: 
        if primes[i]==0:
            k=i*i
            while (k<=n):
                if primes[k]==0:
                    primes[k]=i
                k+=i
        i+=1
    return primes

#22:11 - 22:16
def getFactors(n, primes):
    factors = []
    while primes[n]>0:
        factors.append(primes[n])
        n //= primes[n]
    factors.append(n)
    return factors

n = 17
print (getPrimes(n))
print (getFactors(n,getPrimes(n)))
n = 16
print (getPrimes(n))
print (getFactors(n,getPrimes(n)))
n = 9
print (getPrimes(n))
print (getFactors(n,getPrimes(n)))