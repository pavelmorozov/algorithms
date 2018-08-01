#13:55 -14:37 100%
# need to train to develop faster
def solution(A):
    #max of A
    m = max(A)
    
    #counter
    c = {}
    for v in A:
        if v in c:
            c[v] += 1
        else:
            c[v] = 1
    
    #divisors
    d = {}
    for k in c:
        d[k]={1,k}
        
    #sieve of Eratosthenes
    i = 2
    while i*i <= m:
        j = i
        while j<=m:
            if j in c:
                if not i in d[j]:
                    d[j].add(i)
                    d[j].add(j//i)
            j+=i
        i+=1
    
    #result
    r = [0]*len(A)
    for i, v in enumerate(A):
        r[i] = len(A) - sum([c.get(div, 0) for div in d[v]])
    
    return r

    
A = [2]
print(solution(A))

A = [3,1,2,3,6]
print(solution(A))

