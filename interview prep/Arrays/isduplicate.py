#check if the elements in the array contain duplicates
#this is dpne efficiently by using a hasset in python to store distinct element in hash set

def containsDuplicate(nums):
    hashset = set()

    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False

arr = [1, 2, 3, 4, 5]
status = containsDuplicate(arr)

if status:
    print("contains duplicate")
else:
    print("no duplicates")