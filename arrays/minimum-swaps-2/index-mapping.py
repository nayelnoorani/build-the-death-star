# prints on lines 13, 18 & 22 are kept only for educational purposes
# delete these prints if actually running the code

def minimumSwaps(arr):
    n = len(arr)
    swaps = 0
    sorted_arr = sorted(arr)
    index_map = {value: idx for idx, value in enumerate(arr)}

    for i in range(n):
        if arr[i] != sorted_arr[i]:
            swaps += 1
            swap_idx = index_map[sorted_arr[i]]
            print(f"swapping {arr[i]} and {sorted_arr[i]} at index {i} and {swap_idx}")

            # Update the index_map after the swap
            index_map[arr[i]] = swap_idx
            index_map[sorted_arr[i]] = i
            print(f"index_map: {index_map}")

            # Swap the elements
            arr[i], arr[swap_idx] = arr[swap_idx], arr[i]
            print(f"arr: {arr}")
    
    return swaps

arr0 = [4, 3, 1, 2]
arr1 = [2, 3, 4, 1, 5]
arr2 = [1, 3, 5, 2, 4, 6, 7]

print(minimumSwaps(arr0))
print(minimumSwaps(arr1))
print(minimumSwaps(arr2))