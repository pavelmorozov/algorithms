#72 min found solution on web
def solution(A, B):
    alive_count = 0        # The number of fish that will stay alive
    downstream = []        # To record the fishs flowing downstream

 
    for index, val in enumerate(A):

        if B[index] == 1:
            downstream.append(A[index])
        else:
            while len(downstream) != 0:
                if downstream[-1] < A[index]:
                    downstream.pop()
                else:
                    break
            else:
                alive_count += 1
 
    alive_count += len(downstream)
 
    return alive_count

a=[4,3,2,1,5]
b=[0,1,0,0,0]

print (solution(a,b))

a=[8,3,4,5,4,9]
b=[1,0,0,1,0,1]

print (solution(a,b))

a=[8,3,4,2,5,3]
b=[1,0,0,1,0,1]

print (solution(a,b))