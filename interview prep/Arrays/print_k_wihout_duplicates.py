def removeDuplicates(nums):
    x = 1
    for i in range(len(nums) - 1):
        if (nums[i] != nums[i + 1]):
            nums[x] = nums[i + 1]
            x += 1
    return x

    return rem

arr = [1,1,2]

k = removeDuplicates(arr)
print(arr)
