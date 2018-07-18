N=10
queue = [0]*N
head, tail = 0, 0
def push(x):
    global tail
    queue[tail] = x
    tail = (tail + 1) % N    
def pop():
    global head
    val = queue[head]
    head = (head + 1) % N
    return val
def size():
    return (tail - head + N) % N
def empty():
    return head == tail

push(5)
push(2)
push(7)
print (queue)
push(1)
print (queue)
val = pop()
print (val)
val = pop()
print (val)
print(queue)