# Write the function fun_nth_additive_prime(n) that takes a non-negative int n 
# and returns the nth Additive Prime, which is a prime number such that 
# the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5 
# is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2


all_primes = []
additive_primes = []
def fun_nth_additive_prime(n):
	count = 0
	start_prime = 2
	while count <= n:
		flag = False
		for i in all_primes:
			if(start_prime % i) == 0:
				flag = True
		if(not flag):
			all_primes.append(start_prime)
			if(get_sum(start_prime) in all_primes):
				additive_primes.append(start_prime)
				count += 1
		start_prime += 1
	return additive_primes[n]
def get_sum(n):
	sum = 0
	while n != 0:
		sum += n%10
		n = n//10
	return sum