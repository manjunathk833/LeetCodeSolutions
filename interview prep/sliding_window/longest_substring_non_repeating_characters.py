#https://www.youtube.com/watch?v=wiGpQwVHdE0 https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/

def lengthOfLongestSubstring(s):
    charSet = set()
    l = 0
    res = 0

    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        res = max(res, r - l + 1)
    return res

str = 'abcabcbb'
n = lengthOfLongestSubstring(str)
print("Longest Substring %d for the string %s"%(n,str))