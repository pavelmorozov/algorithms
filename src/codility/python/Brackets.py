#28 min 62% one condition at the end missed
#if len(stack)!=0: return 0
def solution(S):
    stack=[]
    for c in S:
        if c=='(' or c=='[' or c=='{':
            stack.append(c)
        else:
            if len(stack)==0: return 0
            lastChar = stack.pop()
            if not ((lastChar=='{' and c=='}')\
             or (lastChar=='(' and c==')')\
             or (lastChar=='[' and c==']')):
                return 0
    if len(stack)!=0: return 0
    return 1
S = "{[()()]}"
print (solution(S))

S = "([)()]"
print (solution(S))