#https://workat.tech/problem-solving/practice/positive-cumulative-sum


def getCumulativeSum(arr):
    # add your logic here
    sum = 0
    cumarr = []
    for i in arr:
        sum = sum + i
        if sum > 0:
            cumarr.append(sum)
    return cumarr

arr = [1, -2, 3, 4, -6]
s = getCumulativeSum(arr)
print(s)


