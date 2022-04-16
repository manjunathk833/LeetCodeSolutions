'''
reverse a given array or string

Approach 1:
Just swap the first and last elements and then prinnt them
For string convert the array into list and then join and print the reversed string

'''
def reverse(arr, n):
    if n == 0:
        print("empty array")
    for i in range(0, int(n/2)):
        temp = arr[i]
        arr[i] = arr[n-i-1]
        arr[n-i-1] = arr[i]

arr = "Sample String"
n = len(arr)
arr = list(arr)
reverse(arr, n)
arr = "".join(arr)
print("The reversed list is", arr)