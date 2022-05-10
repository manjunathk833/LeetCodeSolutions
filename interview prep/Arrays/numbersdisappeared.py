
'''
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.
'''

'''Approach 1: Use a hash set with ordered elements and compare if all the elements exist or not in the array'''
'''map each value iteratively to it's position and make it as negative and all the positve values index will be the missing elements'''
def findDisappearedNumbers(nums):
    for n in nums:
        i = abs(n) - 1

        nums[i] = -1 *abs(nums[i])

    print(nums)
    res = []
    for i, n in enumerate(nums):
        #print(i, n)
        if n>0:
            res.append((i+1))
    return  res

nums = [4,3,2,7,8,2,3,1]
res = findDisappearedNumbers(nums)
print(res)


'''
Hashset method
tc = O(n)
sc = O(n)

Abs method
tc = O(n)
sc = O(n)
'''
