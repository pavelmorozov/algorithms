
# 30 min but does not get 100% 
# as a 1 element array returns wrong result 
def solution(A):
    if len(A)==1: return 0
    valuesDict = {}
    for i, v in enumerate(A):
        found = valuesDict.get(v)
        if found == None:  valuesDict[v]=1
        else: 
            number = valuesDict.get(v)+1
            if number>len(A)/2: 
                #Dominator here
                return i
            valuesDict[v] = number
    return -1

A =[3,4,3,2,3,-1,3,3]
print(solution(A))
    
A =[3]
print(solution(A))