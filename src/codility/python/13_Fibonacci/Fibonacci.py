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

print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
print(fibonacci(6))

print(fibonacciDynamic(6))