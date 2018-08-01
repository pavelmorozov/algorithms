
# 52 min 44% one of correctness test fail
# performance fail
def getPrimes(N):
    p=[0]*(N+1)
    i=2
    while i*i<=N:
        k=i*i
        while k<=N:
            if p[k]==0:
                p[k]=i
            k+=i
        i+=1
    return p

def getDivisors(N, p):
    #p primes
    divisors = set()
    div = 1
    divisors.add(div)
    i=N
    while i*i>=N:
        div *= p[N] 
        divisors.add(div)
        N//=p[N]
    divisors.add(N)
    div *= N
    divisors.add(div)
    return divisors

def solution(A):
    # find primes limit number (max)
    max=abs(A[0])
    for i in range (1,len(A)):
        if abs(A[i])>max: max=abs(A[i])
    
    primes = getPrimes(max)
    nonDivCounters = [] 
    for i in range (len(A)):
        count = 0
        divisors = getDivisors(A[i], primes)
        for j in range(len(A)):
            if not A[j] in divisors:
                count+=1
        nonDivCounters.append(count)
    
    return nonDivCounters
        
N = 144
print(getPrimes(N))

divisors = getDivisors(N, getPrimes(N))
print(divisors )
print(len(divisors))

A = [3,1,2,3,6]
print(solution(A))