def getPrimes(N):
    p = [0]*(N+1)
    i = 2
    while i*i<=N:
        if p[i]==0:
            j=i*i
            while j<=N:
                if p[j]==0: p[j]+=i
                j+=i
        i+=1
    return p

#p - primes, N is max value
def getPrimeDivisors(p, N):
    pd = set()
    if N==0 or N==1: return pd
    while not p[N]==0:
        pd.add(p[N])
        N//=p[N]
    pd.add(N)
    return pd
    
def solution(A, B):
    max_val = max(A+B)
    primes = getPrimes(max_val)
    equalDivisors = 0
    for i in range(len(A)):
        primeDivisorsA = getPrimeDivisors(primes, A[i])
        primeDivisorsB = getPrimeDivisors(primes, B[i])
        if len(primeDivisorsA)==len(primeDivisorsB):
            count=0
            for v in primeDivisorsA:
                if v in primeDivisorsB: count+=1
            if count == len(primeDivisorsA): equalDivisors+=1
        
    return equalDivisors;
        
    
    
N=5
primes = getPrimes(N)

print(primes)

print(getPrimeDivisors(primes, N))



A = [15,10,3, 25, 0, 1]
B = [75,30,5, 125, 0, 1]

print(solution(A,B))

