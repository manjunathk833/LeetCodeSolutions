#function to find the peak element in python

def find_peak(arr, n):
    #check if the first element is  greater than the second
    if arr[0] > arr[1]:
        return arr[0]
    #check if the last element is greater than the last second
    elif arr[n-1] > arr[n-2]:
        return arr[n-1]
    # check the middle elements
    elif arr[0] < arr[1] and arr[n-1] < arr[n-2]:
        for i in range(1, n-1):
            if(arr[i] > arr[i-1] and arr[i] > arr[i+1]):
                return arr[i]
    # check if all the elements are equal
    else:
        return arr[0]


arr = [2, 3, 4, 1]
n = len(arr)

print("the peak element is ", find_peak(arr,n))

#time complexity O(n) Space Complexity(1) since no additional memory is used
#for efficient solution use binary search method for O(logn) complexity


