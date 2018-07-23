#40 min score 0%, solution 
#return same answer for any input

import platform

def solution(A):
    valuesDict = {}
    dominator = None
    #find leader
    for v in A:
        found = valuesDict.get(v)
        if found == None: valuesDict[v]=1
        else:
            number = valuesDict[v]+1
            if number>len(A)/2: 
                #Dominator here
                dominator=v
            valuesDict[v] = number
    
    if dominator==None: return 0
    
    equiLeadersNumber=0
    foundDominators=0
    dominatorsNumber=valuesDict[dominator]

    for i, v in enumerate(A):
        if v==dominator:
            foundDominators+=1
        if ((i+1)/2)<foundDominators and \
        (len(A)-i-1)/2<(dominatorsNumber-foundDominators):
            equiLeadersNumber+=1
                
    return equiLeadersNumber


print(platform.python_version())
A=[0,0]
print(solution(A))            
A=[4,3,4,4,4,2]
print(solution(A))
A=[4,3,4,4,2,4]
print(solution(A))
A=[4]
print(solution(A))
A=[4,2]
print(solution(A))
