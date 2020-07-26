# Write the function nthLeftTruncatablePrime(n).
# A Left-truncatable prime is a prime which in a given base (say 10) does not contain 0 
# and which remains prime when the leading (left) digit is successively removed. 
# For example, 317 is left-truncatable prime since 317, 17 and 7 are all prime. 
# There are total 4260 left-truncatable primes.
# So nthLeftTruncatablePrime(0) retunearestKaprekarNumber(n)rns 2, and 
# nthLeftTruncatablePrime(10) returns 53.



import math
def isprime(n):
    if n > 1:
        for i in range(2,n):
            if(n % i == 0):
                return False
        return True
def truncatable(n):
    if "0" not in str(n) and isprime(n):
        if (n<10):
            return True
        n = str(n)
        n = int(n[1:len(n)])
        if(isprime(n)):
            return truncatable(n)
        return False
    return False
def fun_nth_lefttruncatableprime(n):
    i = 2
    j = -1
    while(True):
        if truncatable(i):
            j += 1
        if(j ==n):
            return i
        i += 1