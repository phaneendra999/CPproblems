# Given a string str and an integer K, the task is to find the K-th most 
# frequent character in the string. If there are multiple characters that 
# can account as K-th the most frequent character then, print any one of them.


from collections import Counter
def fun_kth_occurrences(s, n):
	s = dict(Counter(s))
	s_values = list(s.values())
	s_values.sort()
	value_to_search = s_values[-2]
	for i in s:
		if(s[i] == value_to_search):
			return i


