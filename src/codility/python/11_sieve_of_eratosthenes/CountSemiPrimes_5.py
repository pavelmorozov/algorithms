#12:17- 13:02 mistake if count not contains divisor- then should be 0
def getCount(A):
    count = {}
    
    for v in A:
        if v in count: count[v]+=1
        else: count[v]=1
    
    return count
            
def getDivisors(A, count):
    
    max_a = max(A)
    #divisors structure
    d = {}
    
    for v in count:
        d[v]={1,v}
        
    #sieve
    i=2
    while i*i <= max_a:
        
        j=i
        while j<= max_a:
            if j in count:
                #!!!
                if i in count: d[j].add(i)
                if j//i in count: d[j].add(j//i)
            j+=i
        i+=1
    return d
    
def solution(A):
    count = getCount(A)
    divisors = getDivisors(A, count)
    
    result = []
    for v in A:
        #!!!!!
        result.append(len(A)-sum([count.get(div,0) for div in divisors[v]]))
        
    return result

A = [2]
print(solution(A))
A = [3,1,2,3,6]
count = getCount(A)
print(count)
divisors = getDivisors(A, count)
print(divisors)
print(solution(A))