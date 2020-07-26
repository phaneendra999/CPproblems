# nthCircularPrime(n) [20 pts]
# Write the function nthCircularPrime that takes a non-negative int n and returns the nth 
# Circular prime, which is a prime number that does not contain any 0's and such that all the 
# numbers resulting from rotating its digits are also prime. The first Circular primes are 2, 3, 
# 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197... To see why 197 is a Circular prime, 
# note that 197 is prime, as is 971 (rotated left), as is 719 (rotated left again).
def isprime(n):
	if(n > 1):
		for i in range(2,n):
			if(n % i == 0):
				return False
		return True
def circularprime(n):
	d = 0
	i = 0
	rem = 0
	sum = 0
	if(n < 10):
		if(isprime(n)):
			return True
		return False
	n = str(n)
	l1 = len(n)
	num = int(n)
	while(i < l1):
		rem = int(num % 10)
		num = int(num/10)
		num = int((rem *(10 ** (l1-1)) + num))
		d = isprime(num)
		sum = sum + d
		i += 1
	if(sum ==l1):
		return True
	return False
def nthcircularprime(n):
	# Your code goes here
	i = 3
	c = 2
	if n ==1:
		return 2
	while(True):
		if(circularprime(i)):
			if c == n:
				return i
		i += 1
		c += 1