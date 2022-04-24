#below is the kadane's algorithm for maximum sum of contiguous sub array

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