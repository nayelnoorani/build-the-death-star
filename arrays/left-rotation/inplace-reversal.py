# Write a function that reverses the array in place
# Python's reversed function takes additional memory
def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotLeft(a, d):
    n = len(a)
    d = d % n # in case d is larger than n
    
    # Step 1: Reverse the first d elements
    reverse(a, 0, d-1) # here the end value is inclusive, unlike slicing

    # Step 2: Reverse the remaining n-d elements
    reverse(a, d, n-1)

    # Step 3: Reverse the whole array
    reverse(a, 0, n-1)

    return a
