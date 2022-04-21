def is_duplicate(arr):
    setcheck = set()
    for i in arr:
        if i in setcheck:
            return True
        setcheck.add(i)
    return False

arr = [5, 4, 3, 1]

status = is_duplicate(arr)

if status:
    print("duplicates exist")
else:
    print("no duplicates")