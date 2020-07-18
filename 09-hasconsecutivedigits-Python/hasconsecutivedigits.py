# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that 
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
	# your code goes here
	if(n ==0):
		return False
	if(n%10 == (n%100)//10):
		return True
	return hasconsecutivedigits(abs(n)//10)