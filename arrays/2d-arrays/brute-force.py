def hourglassSum(arr):
    max_sum = -float('inf') # Initialize with the lowest possible value

    for i in range(4): # There are 4 possible starting rows for hourglasses
        for j in range(4): # There are 4 possible starting columns for hourglasses
            # Calculate the sum of the hourglass
            top = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            middle = arr[i+1][j+1]
            bottom = arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]

            hourglass_sum = top + middle + bottom
            
            # Update max_sum if necessary
            max_sum = max(max_sum, hourglass_sum)

    return max_sum