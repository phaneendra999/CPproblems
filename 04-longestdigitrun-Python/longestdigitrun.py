# longestDigitRun(n) [20 pts]
# Write the function longestDigitRun(n) that takes a possibly-negative int value n and returns 
# the digit that has the longest consecutive 
# run, or the smallest such digit if there is a tie. So, longestDigitRun(117773732) returns 7 (
# because there is a run of 3 consecutive 7's), 
# as does longestDigitRun(-677886).
def lookandsay(a):
	c = 1
	l =[]
	for i in range(1,len(a)+1):
		if(i<len(a) and a[i-1] == a[i]):
			c +=1
		l.append((c,a[i-1]))
		c=1
	return(l)
def longestdigitrun(n):
	# Your code goes here
	n = lookandsay(list(map(int,str(abs(n)))))
	a = b = 0
	for i in n:
		if(i[0] == a and i[1]<b):
			b = i[1]
		elif(i[0] > a):
			a,b = i[0],i[1]
	return b