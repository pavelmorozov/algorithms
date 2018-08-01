#49 min 54%
# I misunderstood the "divided" word,
# and decide that division 
# means at least two parts

# also added small optimization
# with continue in last loop

import math
def solution(A):
    peaks=[]
    for i in range(1, len(A)-1):
        if A[i]>A[i-1] and A[i] > A[i+1]:
            peaks.append(i)
    
    lenFactors = set()
    for i in range (1, int(math.sqrt(len(A)))+1):
        if len(A)%i==0:
            lenFactors.add(i)
            lenFactors.add(int(len(A)/i))
    
    maxIntervalsNumber=0
    for factor in lenFactors:
        if factor<maxIntervalsNumber: continue
        length = len(A)/factor
        intervalsWithPeak = set()
        for i in peaks:
            intervalsWithPeak.add(int(i/length))
        if len(intervalsWithPeak)==factor:
            if maxIntervalsNumber<factor:
                maxIntervalsNumber=factor
    return maxIntervalsNumber

A = [1,2,3,4,3,4,1,2,3,4,6,2]
print (solution(A))

A=[1, 3, 2, 1]
print (solution(A))
 
