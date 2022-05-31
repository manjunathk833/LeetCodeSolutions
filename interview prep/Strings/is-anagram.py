'''
check if the given string is an anagram

Approach: for a given string find the count of each character and add it to a hashmap and then check if the count for each character is the same
'''
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


'''
sort approach

#check if given two strings are anagram or not


#sort function for anagrams
def sortstr(s1):
    n = len(s1)

    for i in range(n):
        for j in range(0, n-i-1):
            if s1[j] > s1[j+1]:
                s1[j], s1[j+1] = s1[j+1], s1[j]
    return


#function to find anagrams
def find_anagram(str1, str2):
    s1 = list(str1)
    s2 = list(str2)

    n1 = len(s1)
    n2 = len(s2)

    if n1 != n2:
        print("strings are not anagrams")
        return
    elif n1 == n2:
        sortstr(s1)
        sortstr(s2)
        for i in range(n2):
            if s1[i] != s2[i]:
                print("strings are not anagrams")
                return
        print("strings are anagrams")
        return


#driver function
s1 = "center"
s2 = "centre"

find_anagram(s1,s2)
'''