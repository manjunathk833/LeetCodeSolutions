
def isAnagram(s, t):
    if len(s) != len(t):
        return False

    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    for c in countS:
        if countS[c] != countT.get(c, 0):
            return False
    return True


s1 = "anagram"
s2 = "gramana"

status = isAnagram(s1, s2)

if status:
    print("String is anagram")
else:
    print("Not an anagram")