'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.



Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
'''

'''
using hashset: can be solved using hash set but uses o(n) memory
Approach: xor anything with itself is 0 and anything xor with 0 is 1 hennce we can xor single number with duplicates to get that number
'''

def singleNumber(nums):
    res = 0
    for num in nums:
        res ^= num
    return res




nums = [4,1,2,1,2]

singleNumber(nums)


#^ is the xor operator