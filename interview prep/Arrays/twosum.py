
def twoSum(nums, target):
    prevMap = {}  # val -> index

    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i

arr = [1, 2, 3, 4]
sum = 3

res = twoSum(arr, sum)
if res:
    print("indices", res)
else:
    print("no sum found")