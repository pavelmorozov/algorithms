def kadane(A):
    max=currentMax=A[0]
    for i in range(1,len(A)):
        if A[i]>A[i]+currentMax: currentMax=A[i]
        else: currentMax=A[i]+currentMax
        if currentMax>max: max=currentMax
    return max

A=[-2, 3, 2, -1]
print(kadane(A))
A=[3,2,-6,3,2,-5,2,7,9]
print(A)
print(kadane(A))
A=[-5, 6, 7, 1, 4, -8, 16]
print(kadane(A))