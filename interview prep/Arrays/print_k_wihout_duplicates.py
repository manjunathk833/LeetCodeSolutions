# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
'''
Approach : Use two pointers left and right and move left everytime right is not equal to right moe right when left is equal and not equal to right
'''
def removeDuplicates(nums):
    l = 1
    for r in range(1, len(nums)):
        if (nums[r] != nums[r-1]):
            nums[l] = nums[r]
            l += 1
    return l

arr = [0,0,1,1,1,2,2,3,3,4]

k = removeDuplicates(arr)
print(k)
print(arr)
