def isPalindrome(s):
    if len (s) <= 1:
         return True
    return s[0] == s[len (s) - 1] and isPalindrome(s[1 : len (s) - 1])

s = input().strip()
if isPalindrome(s):
    print('true')
else:
    print('false')
