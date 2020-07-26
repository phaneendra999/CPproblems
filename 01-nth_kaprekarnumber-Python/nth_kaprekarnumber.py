# Background: a Kaprekar number is a non-negative integer, the representation of whose square 
# can be split into two possibly-different-length parts (where the right part is not zero) 
# that add up to the original number again. For instance, 45 is a Kaprekar number, because 
# 45**2 = 2025 and 20+25 = 45. You can read more about Kaprekar numbers here. The first several 
# Kaprekar numbers are: 1, 9, 45, 55, 99, 297, 703, 999 , 2223, 2728,... 
# With this in mind, write the function nthKaprekarNumber(n) that takes a non-negative int n 
# and returns the nth Kaprekar number, where as usual we start counting at n==0.


import math
def iskapreharnumber(n):
    if n > 0:

        x = int(math.pow(n,2))
        s1 = str(x)
        y = len(str((x)))       
        s2 =""
        s3 =""
        if(len(s1) > 1):
             s2 = s1[0:(y//2)]
             s3 = s1[y//2:y]
             sum1 = (int(s2)) +(int(s3))
        s2 =s1
        sum1 = int(s2)
        if(n == sum1):
            
            return True
            sum1 -= int(s2)
            s2 = s2.strip("0")
            sum1 += int(s2)
            if(sum1 == n):
                return True
            return False


def fun_nth_kaprekarnumber(n):
    c= 0
    i = 2
    if n==0:
        return 1
    while(True):
        if(iskapreharnumber(i)):
            c += 1
        if(c == n):
            break
        i += 1
    return i