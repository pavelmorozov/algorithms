# 27min 100%
def solution(A):
    currentSlice = A[0]
    maxSlice = A[0]
    for i in range(1,len(A)):
        sum = currentSlice+A[i]

        if sum<A[i]: currentSlice = A[i]
        else: currentSlice=sum
        
        if currentSlice>maxSlice: maxSlice = currentSlice
    
    return maxSlice

A = [3,2,-6,4,0]
print(solution(A))
        
A = [7]
print(solution(A))
        
A = [-2,7]
print(solution(A))