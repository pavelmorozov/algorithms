#81 min 100% 
#may be exist 
#more straight 
#forward solution?
def solution(A):
    peaks = []
    lastPeak = 0
    minDistance = 0
    for i in range (1, len(A)-1):
        if A[i]>A[i-1] and A[i]>A[i+1]:
            if not lastPeak == 0:
                dist = i - lastPeak
                if minDistance==0 or minDistance>dist:minDistance=dist
            lastPeak = i
            peaks.append(i)
            
    maxFlags = 0
    for flagsNumber in range(1, len(peaks)+1):
        initPeak = peaks[0]
        flagsSet = 1;
        for i in range(1,len(peaks)):
            dist = peaks[i]-initPeak
            if dist < flagsNumber:
                continue
            else:
                initPeak = peaks[i]
                flagsSet +=1
                if flagsSet==flagsNumber:
                    break

        if flagsSet==flagsNumber:
            maxFlags = flagsNumber

        if flagsSet < flagsNumber:
            break
    
    return maxFlags
                
    
A=[1,5,3]
print(solution(A))


A=[1,5,3,4,3,4,1,2,3,4,6,2]
print(solution(A))

