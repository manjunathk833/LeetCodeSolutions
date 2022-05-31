#below is the kadane's algorithm for maximum sum of contiguous sub array
'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''

'''
Approach: Kadane's algorithm: continuously keep adding elements in the sliding window
if max of until now is less than max at current position 
make max current the max until now

'''
def maxSubArray(nums):
    max_here = max_until_now = nums[0]
    n = len(nums)
    for i in range(1,n):
        max_here = max(nums[i], nums[i] + max_here)
        if max_until_now < max_here:
            max_until_now = max_here
    return max_until_now


nums = [-2,1,-3,4,-1,2,1,-5,4]
ans = maxSubArray(nums)
print(ans)