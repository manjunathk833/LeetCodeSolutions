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