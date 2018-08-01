def gcd(a,b):
    if a==b: return a
    if a>b: return gcd(a-b, b)
    else: return gcd(a, b-a)

print(gcd(24,9))
print(gcd(9,24))