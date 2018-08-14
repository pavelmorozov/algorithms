#O(N)
def sumOfMultiples(a,b,n):
	sum = 0
	for i in range(a,n):
		if i%a==0 or i%b==0:
			sum+=i
	return sum
	
print(sumOfMultiples(3,5,1000))

#much faster