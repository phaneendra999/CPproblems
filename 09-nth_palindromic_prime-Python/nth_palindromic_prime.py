# Write the function fun_nth_palindromic_prime(n) that takes a non-negative int n 
# and returns the nth palindromic Prime, which is a palidrome number such that 
# it is also a prime. For example, 313 is a palindrome and it is prime 
# so 313 is an palindrome Prime. fun_nth_palindrome_prime(0) returns 2



all_primes = []
palidrome_primes = []
def fun_nth_palindromic_prime(n):
	count = 0
	start_val = 2
	while count <= n:
		flag = False
		for i in all_primes:
			if(start_val % i) ==0:
				flag = True
				break
		if(not flag):
			all_primes.append(start_val)
			if(verify(start_val) and (start_val in all_primes)):
				palidrome_primes.append(start_val)
				count += 1

		start_val += 1
	temp = palidrome_primes[n]
	all_primes.clear()
	palidrome_primes.clear()
	return temp
def verify(n):
	n = str(n)
	for i in range(len(n)):
		if(n[i] != n[len(n) - i - 1]):
			return False
		if(i > (len(n) // 2)):
			break
	return True