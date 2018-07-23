import random 
import datetime
#Real test
#50% both correctness and performance
def solution(A, B):

    #all values from flipped A
    aSet=set()
    for i in range(len(A)):
        if A[i]<B[i]:
            #flip all smaller
            tmp = A[i]
            A[i]=B[i]
            B[i]=tmp
        aSet.add(A[i])

    i=1
    while True:
        if not (i in aSet): 
            score = i
            return i
        i+=1

A=[3,2,1,6,5]
B=[4,2,1,3,3]
print(solution(A,B))

A=[1,2,4,3]
B=[1,3,2,3]
print(solution(A,B))

A=[1,2]
B=[1,2]
print(solution(A,B))

def starter(length, printFlag=False):
    A=[]
    B=[]
    for i in range(length):
        A.append(random.randint(2,1000))
        B.append(random.randint(2,1000))
    if printFlag==True:
        print('A: '+' '.join(str(e) for e in A))
        print('B: '+' '.join(str(e) for e in B))
    print()
    print('array length: '+str(length))
    start = datetime.datetime.utcnow()
    print(start)
    print(solution(A,B))
    end = datetime.datetime.utcnow()
    print(end)
    spend = datetime.datetime.timestamp(end)*1000- \
    datetime.datetime.timestamp(start)*1000
    print("Time spend: "+str(spend)+' time per element: '+str(spend/length))

starter(5,True)

starter(100)

starter(10000)

starter(1000000)

