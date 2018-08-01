#

def solution(N, P, Q):
    pList = []
    for i in range(2,int(N/2)+1):
        for j in range(2,i+1):
            if i%j==0 and not i==j: break
        if i==j: pList.append(i)
    
    #print (pList)
    spList=[]
    spFlags = [0] * (N+1)
    for i in range(len(pList)):
        if pList[i]*pList[i]>N: break
        for j in range(i,len(pList)):
            sp = pList[i]*pList[j]
            if sp>N: break
            spList.append(sp)
            spFlags[sp]=1
    
    #print (spList)
    #print (spFlags)
    
    #spList.sort(key=None, reverse=False)

    spAggregation = []
    sum=0
    for i in range(0,len(spFlags)):
        if spFlags[i]==1:
            sum+=1
        spAggregation.append(sum)
    
    #print (spAggregation)
    
    spNumbers=[]
    for i in range(len(P)):
        spNumber = spAggregation[Q[i]]-spAggregation[P[i]-1]
        spNumbers.append(spNumber)
         
    return spNumbers


    
N=26
P=[1,4,16]
Q=[26,10,20]
print (solution(N, P, Q))

N=1
P=[1]
Q=[1]
print (solution(N, P, Q))

N=6
P=[1]
Q=[6]
print (solution(N, P, Q))

