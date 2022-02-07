def count_zeroes(n , k):
    if n<10:
        if n==0:
            return 1
        return 0 
    digit = n % 10
    if digit == k:
        return 1 + count_zeroes(n//10 , k)
    else:
        return count_zeroes(n//10 , k)
n = int(input())
ans = count_zeroes(n , 0)
print(ans)
