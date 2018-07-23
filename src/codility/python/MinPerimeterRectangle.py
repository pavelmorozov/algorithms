#14 min 100%
import math
def solution(N):
    minP=None
    for i in range(1, int(math.sqrt(N)+1)):
        if N%i==0:
            P=(N/i+i)*2
            if minP==None:
                minP=P
            else:
                if P<minP: minP=P
    return int(minP)

print(solution(30))