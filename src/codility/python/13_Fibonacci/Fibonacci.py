#bad because slow!!!
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
        nextF = fib[i - 1] + fib[i - 2]
        if nextF>n: break
        fib.append(nextF) 
    return fib


#print(fibonacci(6))
print(fibonacciDynamic(10))
print(fibonacciDynamicList(10))
print(fibonacciDynamicLessEquals(4181))
