#26min
def solution(S):
    counter = 0
    for c in S:
        if c=='(':counter+=1
        else: counter-=1
        if counter<0: return 0
    if counter>0: return 0
    return 1

S="(()(())())"
print(solution(S))
S="())"
print(solution(S))
S="(((())())"
print(solution(S))