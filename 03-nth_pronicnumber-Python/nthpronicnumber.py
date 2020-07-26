# nthPronicNumber(n) [20 pts]
# Write the function nthPronicNumber that takes a non-negative int n and returns the nth Pronic 
# Number. Pronic number is a number which is the product of two consecutive integers, that is, a 
# number n is a product of x and (x+1).
import math
def ispronic(n):
	i = 1
	while(i <= (math.sqrt(n))):
		if n == i*(i+1):
			return True
		i += 1
	return False

def nthpronicnumber(n):
	# Your code goes here
	if n == 0:
		return 0
	count = 0
	i = 1
	while(True):
		if ispronic(i):
			count += 1
		if count == n:
			return i
		i += 1