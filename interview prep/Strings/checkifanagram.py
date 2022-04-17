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


