stack = []
def push(x):
    stack.append(x)
def pop():
    x = stack.pop()
    return x

print (stack)
push(5)
push(3)
push(7)
print (stack)
last = pop()
print (last)
print (stack)