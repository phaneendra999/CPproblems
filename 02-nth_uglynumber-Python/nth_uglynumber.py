# Write the function nthUglyNumber that takes a non-negative int n and returns the nth Ugly Number. 
# Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 
# 9, 10, 12, 15 shows the few ugly numbers. By convention, nthUglyNumber(0) will give 1.

def isdivides(a,b):
    while a % b == 0:
        a = a / b
    return a
def isugly(n):
    if n == 2 or n == 3 or n == 5:
        return True
    n = isdivides(n,2)
    n = isdivides(n,3)
    n = isdivides(n,5)
    if n == 1:
        return True
    return False
def fun_nth_uglynumber(n):
    i = 1
    count = 1
    while(n >= count):
        i += 1
        if(isugly(i)):
            count += 1
    return i