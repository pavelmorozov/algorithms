# 21:06 - 21:39
def getPrimes(n):
    primes = [0] * (n+1)
    i=2
    while i*i <= n:
        if primes[i]==0:
            k = i*i
            while (k<=n):
                if primes[k]==0:
                    primes[k]=i
                k=k+i
        i+=1
    return primes

def getFactors(n, primes):
    factors = []
    while True:
        if primes[n]==0:
            factors.append(n)
            break
        else: factors.append(primes[n]) 
        n=n//primes[n]
    return factors

n = 9
primes = getPrimes(n)
print(n)
print(primes)
print(getFactors(n, primes))

