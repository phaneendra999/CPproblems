# Write the function hasnoprimes(L) that takes a 2d list L of integers, 
# and returns True if L does not contain any primes, and False otherwise.


def fun_hasnoprimes(l):
	for i in l:
		for j in i:
			if(j == 2):
				continue
			else:
				for k in range(2,j):
					if(j % k == 0):
						return False 
	return True

