'''
SIMPLE SOLN:

Count 0s, 1s and 2s and then print them in order

'''


def countandsort(arr, n):
    count0 = 0
    count1= 0
    count2 = 0

    for i in range(0,n):
        if arr[i] == 0:
            count0 = count0 + 1
        elif arr[i] == 1:
            count1 = count1 + 1
        elif arr[i] == 2:
            count2 = count2 + 1
        i = 0
    for i in range(i,count0):
            arr[i] = 0
    print("i after first iteeration", i)
    for i in range(i, count0 + count1):
            arr[i] = 1
    print("i after first 2nd iteeration", i)
    for i in range(i, n):
            arr[i] = 2
    print("i after 3rd iteeration", i)
    return



arr = [0, 1, 2, 0, 1, 2, 0]
n = len(arr)

countandsort(arr,n)

print("sorted arry", arr)
