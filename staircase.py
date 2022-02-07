def findStep(n):
    if ( n == 0 ):
        return 1
    elif (n < 0):
        return 0
 
    else:
        return findStep(n - 1) + findStep(n - 2) + findStep(n - 3)
n = int(input())
print(findStep(n))
