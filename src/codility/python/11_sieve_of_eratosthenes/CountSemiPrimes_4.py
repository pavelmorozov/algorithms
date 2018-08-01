#11:43
def getSemiPrimes(N):
    primes = [True]*(N+1)

    i = 2
    while i*i <= N:
        if primes[i]==True:
            for j in range (i*i, N, i):
                if primes[j] == True:
                    primes[j] = False
        i+=1
    
    semiPrimes = [False]*(N+1)
    i = 2
    while i*i <= N:
        
        if primes[i]:
        
            for j in range (i*i, N+1, i):
                if primes[j//i]==True:
                    semiPrimes[j]=True
        i+=1
    
    return semiPrimes

def solution(N, P, Q):
    semiPrimes = getSemiPrimes(N)
    spAgg = [0]*(N+1)
    
    for i in range(1,N+1):
        if semiPrimes[i]==True:
            spAgg[i]=spAgg[i-1]+1
        else:
            spAgg[i]=spAgg[i-1]
    
    result = []
    
    for i in range(len(P)):
        diff = spAgg[Q[i]]-spAgg[P[i]-1] 
        result.append(diff)
    
    return result

print(getSemiPrimes(26))

N=26
P=[1,4,16]
Q=[26,10,20]
print (solution(N, P, Q))
