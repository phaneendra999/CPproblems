# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 



def fun_set_kth_digit(n, k, d):
	status= True
	if(n<0):
		status = False
	temp = abs(n)
	leftnum = temp //(10 **(k+1))
	rightnum = temp % (10**k)
	if(not status):
		return - 1* ((10**k) *((leftnum * 10) + d) + rightnum)
	return (((10**k)*((leftnum*10) + d)) + rightnum)

