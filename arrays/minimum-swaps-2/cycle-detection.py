'''
Conceptual framing of the cycle detection method:

It focuses on detecting and resolving cycles by recognizing the misplaced 
elements and counting the minimal swaps required to sort the cycle. It's 
often framed in terms of permutations and sorting.


Conceptual framing of the graph-based approach:

This method views the problem as a graph traversal. Each index of the array 
represents a node and each node points to another node (index) based on the 
value in the array. The goal is to visit all nodes and resolve each cycle 
in the graph.

'''



def minimumSwaps(arr):
    n = len(arr)
    visited = [False] * n
    swaps = 0

    print(f"Initial array: {arr}")
    print(f"Visited array: {visited}")

    for i in range(n):
        print(f"\n-- Starting new iteration for index {i} --")
        if visited[i] or arr[i] == i + 1:
            print(f"Index {i} has already been visited or its value is correct. Skipping...")
            continue

        cycle_size = 0
        x = i

        print(f"Starting new cycle detection from index {i}")
        while not visited[x]:
            print(f"Visiting index {x}, element {arr[x]}")
            visited[x] = True
            x = arr[x] - 1
            cycle_size += 1
            print(f"Moved to index {x}, cycle size now {cycle_size}")

        if cycle_size > 0:
            swaps += (cycle_size - 1)
            print(f"Cycle completed with size {cycle_size}. Total swaps so far: {swaps}")

    print(f"\nFinal visited array: {visited}")
    print(f"Total swaps needed: {swaps}")
    return swaps

arr0 = [4, 3, 1, 2]
arr1 = [2, 3, 4, 1, 5]
arr2 = [1, 3, 5, 2, 4, 6, 7]

print(minimumSwaps(arr0))
print(minimumSwaps(arr1))
print(minimumSwaps(arr2))