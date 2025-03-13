def binary_search(arr, item):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low+high)//2
        guess = arr[mid]
        if (item == guess):
            return mid
        elif( item > guess):
            low = mid + 1
        else:
            high = mid - 1
    return None

print(binary_search([1,2,3,4,5],2))
