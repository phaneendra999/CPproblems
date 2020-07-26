# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.

def isprime(n):
	for i in range(2,n):
		if(n%i == 0):
			return False
	return True
def primefac(a):
	i =2
	flag = 0
	l = a//2
	while(l>=i):
		if(isprime(i) and a%i == 0):
			flag = 1
			if(a%(i**2) != 0):
				return False
		i +=1
	if(flag == 0):
		return False
	return True
def nthpowerfulnumber(n):
	# Your code goes here
	if n ==0:
		return 1
	i = 0
	j = 2
	while(i<n):
		if(primefac(j)):

			i += 1
		j += 1
	return j-1
	
