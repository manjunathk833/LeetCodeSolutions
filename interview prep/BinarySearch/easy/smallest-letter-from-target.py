'''Given a characters array letters that is sorted in non-decreasing order and a character target, return the smallest character in the array that is larger than target.

Note that the letters wrap around.

For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'.

https://leetcode.com/problems/find-smallest-letter-greater-than-target
'''


def find_letter(letters, target):
    n = len(letters)
    low = 0
    high = n-1
    mid = (low + high)//2
    while low != high:
        if target >= letters[mid]:
            low = mid + 1
            mid = (low + high)//2
        elif target < letters[mid]:
            high = mid
            mid = (low + high)//2
    return letters[low]


arr = ["c","f","j"]
target = "c"
op = find_letter(arr, target)
print(op)