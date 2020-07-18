# Write the function nthHappyNumber(n) which takes a non-negative integer 
# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:
# assert(nthHappyNumber(0) == 1)
# assert(nthHappyNumber(1) == 7)
# assert(nthHappyNumber(2) == 10)
# assert(nthHappyNumber(3) == 13)
# assert(nthHappyNumber(4) == 19)
# assert(nthHappyNumber(5) == 23)
# assert(nthHappyNumber(6) == 28)
# assert(nthHappyNumber(7) == 31)

def ishappynumber(n):
	def sumofsquares(n1):
		sum = 0
		while n1 >0:
			rem = n1 % 10
			sum = sum + (rem ** 2)
			n1 = n1//10
		return sum
	list = []
	while sumofsquares(n) not in list:
		result = sumofsquares(n)
		if(result ==1):
			return True
		list.append(result)
		n = result
	return False
def fun_nth_happy_number(n):
	li = [i for i in range(100) if ishappynumber(i)]
	return li[n]
