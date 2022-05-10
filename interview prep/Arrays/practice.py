
def twoSum(arr, sum):
    sumMap = {}
    for i, n in enumerate(arr):
        diff = sum - n
        if diff in sumMap:
            return [sumMap[diff], i]
        sumMap[n] = i


arr = [1, 2, 3, 4]
sum = 3

res = twoSum(arr, sum)
if res:
    print("indices", res)
else:
    print("no sum found")