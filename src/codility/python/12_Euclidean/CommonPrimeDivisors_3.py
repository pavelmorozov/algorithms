def gcd(a,b):
    if a%b == 0: return b
    else: return gcd(b,a%b)
    
def removeCommonDivisors(a, b):
    while a!=1:
        gcd_a = gcd(a,b)
        if gcd_a==1: break
        a/=gcd_a
    return a

def checkSamePrimeDivisors(a,b):
    gcd_a = gcd(a,b)
    rest = removeCommonDivisors(a, gcd_a)
    if rest!=1:return False
    rest = removeCommonDivisors(b, gcd_a)
    if rest!=1:return False
    return True
        
def solution(A, B):
    count=0
    for a,b in zip(A,B):
        if checkSamePrimeDivisors(a,b):
            count+=1
    return count

A = [15,10,3]
B = [75,30,5]

print(solution(A, B))

A = []
B = []

print(solution(A, B))

A = [1]
B = [1]

print(solution(A, B))


print(checkSamePrimeDivisors(15, 75))
print(checkSamePrimeDivisors(15, 12))

print(gcd(12,15))
print(removeCommonDivisors(15, 12))
print(removeCommonDivisors(75, 15))