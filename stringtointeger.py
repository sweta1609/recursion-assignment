def stringtoint(str):
    if len(str) == 1:
        return ord(str[0])-ord('0')
    y = stringtoint(str[1:])
    x = ord(str[0])-ord('0')
    x = x*(10**(len(str)-1))+y
    return int(x)
str = input().strip()
ans = stringtoint(str)
print(ans)
