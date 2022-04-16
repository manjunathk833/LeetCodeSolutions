'''
An array contains both positive and negative numbers in random order. Rearrange the array elements so that all negative numbers appear before all positive numbers.

Examples :

Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
Output: -12 -13 -5 -7 -3 -6 11 6 5
'''

# def move_neg(arr, n):
#     j = 0
#     for i in range(n):
#         if arr[i] < 0:
#             temp = arr[i]
#             arr[i] = arr[j]
#             arr[j] = temp
#             j = j + 1
#     return

#the flag algorithm implemented for two groups below
def move_neg(arr, n):
    low = 0
    high = n-1
    while low <= high:
        if arr[low] > 0:
            arr[low], arr[high] = arr[high], arr[low]
            low = low + 1
            high = high - 1
        else:
            low = low + 1
    return


arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
n = len(arr)

move_neg(arr, n)

print("Rearranged elements are", arr)