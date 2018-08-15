from queue import Queue;

#100 % very hard, copied from web and checked few times
def fibonacciDynamic(n):
    fib = [0,1]
    for i in range(2, n + 2):
        fib.append(fib[i - 1] + fib[i - 2])
        if fib[i]>n: break
    return fib[::-1]

def solution(A):
    class Status(object):
        # Object to store the status of attempts
        __slots__ = ('position', 'moves')
        def __init__(self, pos, moves):
            self.position = pos
            self.moves = moves
            return

    fibonacci = fibonacciDynamic(len(A)+1) # Fibonacci numbers
    
    
    statusQueue = Queue()
    statusQueue.put(Status(-1,0))
    
    #statusQueue = []    # Initially we are at position
                                    # -1 with 0 move.
    accessed = [False] * len(A) # Were we in this position before?
    while True:
        if statusQueue.qsize()==0:
            # There is no unprocessed attemp. And we did not
            # find any path yet. So no path exists.
            return -1
        # Obtain the next attemp's status
        status = statusQueue.get()

        #currentPos = currentStatus.position
        #currentMoves = currentStatus.moves
        
        # Based upon the current attemp, we are trying any
        # possible move.
        for length in fibonacci:
            
            if length==0: continue
            
            destination = status.position + length
            
            if destination == len(A):
                # Ohhh~ We are at the goal position!
                return status.moves + 1
            elif destination > len(A) \
                    or A[destination] == 0 \
                    or accessed[destination]:
                # Three conditions are moving too far, no
                # leaf available for moving, and being here
                # before respectively.
                # PAY ATTENTION: we are using Breadth First
                # Search. If we were here before, the previous
                # attemp must achieved here with less or same
                # number of moves. With completely same future
                # path, current attemp will never have less
                # moves to goal than previous attemp. So it
                # could be pruned.
                continue
            # Enqueue for later attemp.
            statusQueue.put(
                Status(destination, status.moves+1))
            accessed[destination] = True
            
A = [1]
print (solution (A))
            
A = []
print (solution (A))

A = [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0]
print (solution (A))

A = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print (solution (A))
