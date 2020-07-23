# Background: we can represent a polynomial as a list of its coefficients. For example, [2, 3, 0, 4] could represent 
# the polynomial 2x3 + 3x2 + 4. With this in mind, write the function multiplyPolynomials(p1, p2) which takes two 
# lists representing polynomials as just described, and returns a third list representing the polynomial which is 
# the product of the two. For example, multiplyPolynomials([2,0,3], [4,5]) represents the problem (2x**2 + 3)(4x + 
# 5), and:    (2x**2 + 3)(4x + 5) = 8x**3 + 10x**2 + 12x + 15
# And so this returns the list [8, 10, 12, 15].

def multipolynomials(p1, p2):
	# Your code goes here
	l1 = len(p1) - 1
	l2 = len(p2) - 1
	first = {}
	second = {}
	res = {}

	for i in p1:
		first[l1] = i
		l1 = l1 -1
	for i in p2:
		second[l2] = i
		l2 = l2 -1

	for a in first.items():
		for b in second.items():
			r = a[0] + b[0]
			m = a[1] * b[1]

			if(r not in res):
				res[r] = m
			else:
				res[r] += m
	return list(res.values())