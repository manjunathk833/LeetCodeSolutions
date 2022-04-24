def check_pal(str, n):
    l = 0
    r = n-1
    while l < r:
        while l<r and not check_alnum(str[l]):
            l += 1
        while l<r and not check_alnum(str[r]):
                r -= 1
        if str[l].lower() != str[r].lower():
            return False
        l += 1
        r -= 1
    return True



def check_alnum(ch):
    if ord('A') <= ord(ch) <= ord('Z') or ord('a') <= ord(ch) <= ord('z') or ord('1') <= ord(ch) <= ord('9'):
        return True
    else:
        return False

str = 'maam'
n = len(str)
st = check_pal(str, n)

if st:
    print("Palindrome")
else:
    print("Not a palindrome")