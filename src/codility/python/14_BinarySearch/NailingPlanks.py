def firstNail(begin,end,C,prevResult):
    
    minInd = 0
    maxInd = len(C)-1
    
    nailed = -1 #index of first most nail
    
    while minInd<=maxInd:
        mid = (minInd+maxInd)//2
        if C[mid][1]<begin: minInd = mid+1
        elif C[mid][1]>end: maxInd = mid-1
        else:
            nailed = mid
            if C[nailed][0]<=prevResult: return C[nailed][0]
            #check will it be possible to get smaller nail index?
            maxInd = mid-1

    if nailed==-1: return -1
        
    # nailed is the index in sorted C
    # but it could be not the first in initial 
    # list. Check further nails init index:
    next = nailed+1
    result = C[nailed][0]
    while next<len(C)-1 and C[next][1]<=end:
        result = min (result, C[next][0])
        if result<prevResult: return result
        next+=1
        
    return result

def solution(A, B, C):
    #Sort nails
    CSorted = sorted(enumerate(C), key = lambda x: x[1]) 
    lastNail=-1;
    for i in range(len(A)):
        f = firstNail(A[i],B[i],CSorted, lastNail)
        if lastNail<f: 
            lastNail=f
        elif f<0: return -1
    return lastNail+1

A=[1,4,5,4]
B=[4,5,9,10]
C=[4,10,5,7,2]
print(solution(A,B,C))

A=[4]
B=[6]
C=[2]
print(solution(A,B,C))

A=[1,4,5,8,15]
B=[4,5,9,10,20]
C=[4,6,7,10,2]
print(solution(A,B,C))

A=[1,4,5,8]
B=[4,5,9,10]
C=[4,6,7,10,2]
print(solution(A,B,C))

A=[1]
B=[4]
C=[4]
print(solution(A,B,C))

A=[1]
B=[4]
C=[5]
print(solution(A,B,C))

A=[1]
B=[2]
C=[2]
print(solution(A,B,C))