#100% 13 min
def getGcd(N,M):
    if N%M==0: return M
    else: return getGcd(M,N%M)

def getLcm (N,M):
    #find gcd
    gcd = getGcd(N,M)
    lcm = N*M/gcd
    return lcm

def solution(N, M):
    #find lcm
    lcm = getLcm(N,M)
    #result = lcm/M
    result = int(lcm/M)
    return result
    
    

N = 10
M = 5
print(solution(N,M))

N = 10
M = 4
print(solution(N,M))

N = 1
M = 1
print(solution(N,M))

N = 12
M = 3
print(solution(N,M))