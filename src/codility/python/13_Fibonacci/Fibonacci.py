def fibonacci(n):
    if (n <= 1):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

#O(n)
def fibonacciDynamic(n):
    fib = [0] * (n + 1)
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]

def fibonacciDynamicList(n):
    fib = [0] * (n + 1)
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib

def fibonacciDynamicLessEquals(n):
    fib = [0,1]
    for i in range(2, n + 2):
        fib.append(fib[i - 1] + fib[i - 2])
        if fib[i]>=n: break 
    return fib


#print(fibonacci(6))
#print(fibonacciDynamic(6))
#print(fibonacciDynamicList(6))
print(fibonacciDynamicLessEquals(2))
