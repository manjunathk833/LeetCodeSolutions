#function to find the kth smallest element

def smallest(arr, k):
    arr.sort()
    return arr[k-1]

arr = [2, 1, 3, 4, 5, 8, 11, 34, 6, 8]

ele = smallest(arr, 2)

print(ele)
