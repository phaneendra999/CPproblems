# Note: please do not start this problem prior to completing previous problem. 
# Bearing in mind the definition of Kaprekar Number from above problem, write the function 
# nearestKaprekarNumber(n) that takes an int value n and returns the Kaprekar number 
# closest to n, with ties going to smaller value. For example, nearestKaprekarNumber(49) returns 45, 
# and nearestKaprekarNumber(51) returns 55. And since ties go to the smaller number, 
# nearestKaprekarNumber(50) returns 45. 
# Note: as you probably guessed, this also cannot be solved by counting up from 0, 
# as that will not be efficient enough to get past the autograder. 
# Hint: one way to solve this is to start at n and grow in each direction until you find a Kaprekar number.



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

def fun_nearestkaprekarnumber(n):
    i = 0
    j = 2
    while(True):
        if iskapreharnumber(j):
            if(j>= n):
                if(abs(j-n) < abs(i-n)):
                    return j
                elif(abs(j-n) > abs(i-n)):
                    return i
                elif(abs(j-n) == abs(i-n)):
                    return min(i,j)
            i = j
        j += 1