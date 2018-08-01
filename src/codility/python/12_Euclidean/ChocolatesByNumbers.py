#50% - low performance
def solution(N, M):
    circle = [True] * N
    i = 0
    count = 0
    while circle[i]==True:
        circle[i] = False
        count+=1
        i = (i+M) % N
		
    return count

N = 10
M = 4
print(solution(N,M))