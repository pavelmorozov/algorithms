def solution(A, B):
    downstream=[]

    for i in A:
        if B[i]==1:
            downstream.append(i)
        else:
            if




        if len(stack)>0:    
            size=A[downstream[-1]]
            direction=B[downstream[-1]]
            if direction>B[i]:
                if size>A[i]: stack.append(i)
                else: stack.append(stack[i])
        else:
            downstream.append(i)


a=[4,3,2,1,5]
b=[0,1,0,0,0]