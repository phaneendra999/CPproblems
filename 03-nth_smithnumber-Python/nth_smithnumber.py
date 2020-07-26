# Write the function nthSmithNumber that takes a non-negative int n 
# and returns the nth Smith number, where a Smith number is a composite (non-prime) 
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1). 
# Note that if a prime number divides the Smith number multiple times, its digit sum 
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is 
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22

def sum2(n):
    if(len(str(n)) == 1):
        return n
    s = 0
    n1 = str(n)
    for i in n1:
        s += int(i)
    return s
def sum1(l):
    s = ""
    for i in range(len(l)):
        s+= str(l[i])
    s = list(s)
    num = list(map(int,s))
    return sum(num)

def isprime(n):
    if n>1:
        for i in range(2,n):
            if(n % i == 0):
                return False
        return True

def smithnumber(n):
    p = n
    i = 2
    l =[]
    while(n > 1):
        if(isprime(i)):
            while(n % i == 0 and n > 1):
                l.append(i)
                n //= i
        i += 1
    if(sum2(p) == sum1(l)):
        return True
    return False


def fun_nth_smithnumber(n):
    i = -1
    j = 2
    while(i < n):
        if(isprime(j) != True):
            if(smithnumber(j)):
                i += 1
        j += 1
    return j-1