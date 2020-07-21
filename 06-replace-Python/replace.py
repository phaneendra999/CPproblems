# Without using the builtin method s.replace(), 
# write its equivalent. Specifically, write the function 
# replace(s1, s2, s3) that returns a string equal to 
# s1.replace(s2, s3), but again without calling s.replace().

def strings(x,y,z):
	a = ""
	for i in range (z,len(x)):
		if(i != len(x) - 1):
			a += x[i] + y
		a += x[i]
	return a
def fun_replace(s1, s2, s3):
	x = s1.split(s2)
	if(len(x[0]) == len(s1)):
		return s1
	y = ""
	i = 0
	if(len(x[0]) == len(s1)):
		i = 1
		y += s3
	y += strings(x,s3,i)
	return y

