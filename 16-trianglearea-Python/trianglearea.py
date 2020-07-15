# trianglearea(s1, s2, s3)[5pts]
# Write the function trianglearea(s1, s2, s3) that takes 3 floats/ints and returns the area of the
# triangle that has those lengths of its side. If no such triangle exists, return 0. Hint: you
# will probably wish to use Heron's Formula.

import math
def trianglearea(s1, s2, s3):
	# your code goes here
	if((s1 == s2== s3) or (s1+s2 > s3 and s2+s3 >s1 and s1+s3 > s2)):
		s = (s1+s2+s3)/2 
		return math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
	return 0