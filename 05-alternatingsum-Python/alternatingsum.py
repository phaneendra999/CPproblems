# Write the function alternatingSum(a) that takes a list of numbers and returns the 
# alternating sum (where the sign alternates from positive to negative or vice versa). 
# For example, alternatingSum([5,3,8,4]) returns 6 (that is, 5-3+8-4). If the list is empty, return 0.



result = 0
def fun_alternatingsum(a): 
	if(len(l) == 0):
		return 0
	return summation(l)

status = True
def summation(l):
	global result,status
	if(len(l)==0):
		temp = result
		result = 0
		status = True
		return temp
	if(status):
		result += l.pop(0)
		status = False
	result -= l.pop(0)
	status = True
	return summation(l)


