#7 minutes 57 % performance problem
# updated to efficient solution (100%)
import math
def solution(N):
    factorsSet = set()
    for i in range (1,int(math.sqrt(N)+1)):
        if N % i == 0:
            factorsSet.add(i)
            factorsSet.add(N/i)
    return len(factorsSet)
print(solution(24))
print(solution(1))