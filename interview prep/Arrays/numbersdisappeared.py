def findDisappearedNumbers(nums):
    l = len(nums)
    arrhash = dict.fromkeys(range(1, l+1), 0)
    #print(arrhash[0])

    for i in arrhash:
        for j in range(l):
            if nums[j] == i:
                arrhash[i] = 1 + arrhash[i]
    #print(arrhash)
    res = []
    for i in arrhash:
        if arrhash[i] == 0:
            res.append(i)
    return res

nums = [4,3,2,7,8,2,3,1]
res = findDisappearedNumbers(nums)
print(res)