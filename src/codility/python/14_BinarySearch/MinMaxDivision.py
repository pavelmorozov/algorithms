def checkIntervals(A, sumLimit):
    sum=0
    intervalsNumber=1
    for val in A:
        
        if sum+val > sumLimit:
            intervalsNumber+=1;
            sum=val
        else:
            sum+=val
    
    return intervalsNumber;
    

def solution(K, M, A):
    minVal = max(A)
    maxVal = sum(A)
    
    res = maxVal
    
    while minVal<=maxVal:
        avgVal = (minVal+maxVal)//2
        intervalsNumber = checkIntervals(A,avgVal)
        if intervalsNumber>K:
            minVal = avgVal+1
        else:
            maxVal = avgVal-1
            res = avgVal
    
    return res
    

A = [2,1,5,1,2,2,2]
M=5
K=10

print (solution(K,M,A))
