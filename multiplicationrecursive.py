import math
def mul_n(m , n):
    if n == 0:
        return 0
    return m*(n-1) + m
m = int(input())
n = int (input())
ans = mul_n(m , n)
print(ans)
