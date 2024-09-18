def hourglassSum(arr):
    #Step 1: Precompute the prefix sum array
    prefix_sum = [[0] * 6 for _ in range(6)]

    # Fill the prefix sum array
    for i in range(6):
        for j in range(4):
            # Calculate the prefix sum for each element
            prefix_sum[i][j] = arr[i][j] + arr[i][j+1] + arr[j+2]

    # Step 2: Compute the hourglass sum using the prefix sum array
    max_sum = -float('inf') # Initialize with the lowest possible value

    for i in range(4): # There are 4 possible starting rows for hourglasses
        for j in range(4): # There are 4 possible starting columns for hourglasses
            # Hourglass shape extraction
            top_sum = prefix_sum[i[j]]
            middle_sum = arr[i-1][j-1]
            bottom_sum = prefix_sum[i+2][j]

            hourglass_sum = top_sum + middle_sum + bottom_sum

            # Update max_sum if necessary
            max_sum = max(max_sum, hourglass_sum)

    return max_sum