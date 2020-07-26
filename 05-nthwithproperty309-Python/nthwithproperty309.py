# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.
def property_s(i):
	x = i ** 5
	str1 = str(x)
	y = len(str1)
	l =[]
	if(len(str1) >= 9):
		for each in str1:
			l.append(each,str1.count(each))
		l = sorted(set(l))
		if(len(l) == 10):
			return True
		return False
	return False

def nthwithproperty309(n):
	# Your code goes here
	if n == 0:
		return 309
	c =0
	i = 310
	while(True):
		if(property_s(i) == True):
			c+= 1
			if c==n:
				return i
			i += 1
		i+=1
		