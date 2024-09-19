def minimumSwaps(arr):
    n = len(arr)
    swaps = 0
    sorted_arr = sorted(arr)
    index_map = {value: idx for idx, value in enumerate(arr)}

    for i in range(n):
        if arr[i] != sorted_arr[i]:
            swaps += 1
            swap_idx = index_map[sorted_arr[i]]

            # Update the index_map after the swap
            index_map[arr[i]] = swap_idx
            index_map[sorted_arr[i]] = i

            # Swap the elements
            arr[i], arr[swap_idx] = arr[swap_idx], arr[i]
    
    return swaps