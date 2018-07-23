# 22 min 100%
def solution(A):
    currentProfit = 0
    maxProfit=0
    for i in range(1,len(A)):
        currentProfit = A[i] - A[i-1] + currentProfit
        if currentProfit<0: currentProfit = 0
        if currentProfit>maxProfit: maxProfit = currentProfit
    return maxProfit

A=[23171,21011,21123,21366,21013,21367]
print(solution(A))

A=[0]
print(solution(A))

A=[10, 20]
print(solution(A))

A=[-10, -20]
print(solution(A))