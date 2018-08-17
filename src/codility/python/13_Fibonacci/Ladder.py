#%2**32 used to make result numbers small
#because large numbers addition will take O(L)
#and small numbers will help to have O(1) instead
def fibonacciDynamicMod2pow32(n):
    fib = [0] * (n + 1)
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = (fib[i - 1] + fib[i - 2])%2**32
    return fib

def solution(A, B):
    maxVal = len(A)
    F = fibonacciDynamicMod2pow32(maxVal+1)
    res = [0]*(len(A))
    for i in range(len(A)):
        res[i] = F[A[i]+1]%2**B[i]
    
    return res

A = [1]
B = [1]
print(solution(A,B))

A = [4,4,5,5,1]
B = [3,2,4,3,1]
print(solution(A,B))