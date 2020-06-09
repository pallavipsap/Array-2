
# this code executes in time complexity O(n-2)
# space complexity : O(1)
# the idea is to initialise the elements to initial min and max value and then compare with rest of the element that is n-2 elements
def min_max(arr) -> two_values:

    # If there is only one element then return it as min and max both
    n = len(arr)
    minmax = pair() # tuple
    if n == 1:
        minmax.max = arr[0]
        minmax.min = arr[0]
        return minmax

if arr[0] > arr[1]:
        minmax.max = arr[0]
        minmax.min = arr[1]
    else:
        minmax.max = arr[1]
        minmax.min = arr[0]

    for i in range(2, n): # executes n-2 times
        if arr[i] > minmax.max:
            minmax.max = arr[i]
        elif arr[i] < minmax.min:
            minmax.min = arr[i]

    return minmax


arr = [1000, 11, 445, 1, 330, 3000]
min_max(arr)