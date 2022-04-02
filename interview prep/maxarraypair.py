#driver method

def max_product(arr, n):
#initialize default values
    if n < 2:
        print("please enter more inputs")
    elif n == 2:
        print(arr[0] , " " , arr[1])

    #initialise positive and negative values
    pa = pb = na = nb = 0

    #compare successive elements and find the largest product pair
    for i in range(0, n):
        if(arr[i] > pa):
            pb = pa
            pa = arr[i]
        elif(arr[i] > pb):
            pb = arr[i]

        if(arr[i] < 0 and abs(arr[i]) > na):
            nb = na
            na = arr[i]
        elif(arr[i] < 0 and abs(arr[i]) > nb):
            nb = arr[i]
    if(na * nb > pa * pb):
        print("max product:" , na , " ", nb)
    else:
        print("max product:" , pa, " ", pb)
arr = [4, 3, 2, 1, 5, -6, -7]
n = len(arr)
max_product(arr, n)



