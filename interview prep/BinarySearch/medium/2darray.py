#Given a 2d matrix search for a given element using binary search

def bin_search(arr, ele):
    row, col = len(arr), len(arr[0])
    top, bot = 0, row-1
    while top <= bot:
        midrow = (top + bot) // 2
        if ele > arr[midrow][-1]:
            top = midrow + 1
        elif ele < arr[midrow][0]:
            bot = midrow - 1
        else:
            break

    if not top <= bot:
        return False
    beg, end = 0, col-1

    while beg <= end:
        midcol = (beg + end) // 2
        if ele == arr[midrow][midcol]:
            return [midrow+1, midcol+1]
        elif ele > arr[midrow][midcol]:
            beg = midcol + 1
        elif ele < arr[midrow][midcol]:
            end = midcol - 1

    return False


#array is sorted
arr = [[1,2,3], [4,5,6], [7,8,9]]
ele = 7

position = bin_search(arr, ele)

if position:
    print("element found in position", position)
else:
    print("element not found")
