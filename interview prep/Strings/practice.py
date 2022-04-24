def is_anagram(arr1,arr2):
    count1 = {}
    count2 = {}
    if len(arr1) != len(arr2):
        return False


    for i in range(len(arr1)):
        count1[arr1[i]] = 1 + count1.get(arr1[i], 0)
        count2[arr2[i]] = 1 + count2.get(arr2[i], 0)


    for c in count1:
        if count1[c] != count2[c]:
            return False
    return True

arr1 = "anagram"
arr2 = "gramana"

status = is_anagram(arr1,arr2)
if status:
    print("yes")
else:
    print("no")