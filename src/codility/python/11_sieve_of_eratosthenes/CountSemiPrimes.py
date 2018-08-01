#45 min 55% - very long. 
# performance problem.
# Find more 
# efficient solution.

def solution(N, P, Q):
    pList = []
    for i in range(2,int(N/2)+1):
        for j in range(2,i+1):
            if i%j==0 and not i==j: break
        if i==j: pList.append(i)
    
    #print (pList)
    spList=[]
    for i in range(len(pList)):
        for j in range(i,len(pList)):
            sp = pList[i]*pList[j]
            if sp>N: 
                break
                break
            spList.append(sp)
    
    spList.sort(key=None, reverse=False)
    #print (spList)
    
    
    spNumbers=[]
    for i in range(len(P)):
        spNumber = 0
        for sp in spList:
            if sp>=P[i] and sp <= Q[i]:
                spNumber+=1
            if sp > Q[i]: break
        spNumbers.append(spNumber)
         
    return spNumbers
    
N=26
P=[1,4,16]
Q=[26,10,20]
print (solution(N, P, Q))

N=6
P=[1]
Q=[6]
print (solution(N, P, Q))