def gcd(a,b):
    if a%b==0: return b
    else: return gcd (b,a%b)

print(gcd(24,9))
print(gcd(9,24))