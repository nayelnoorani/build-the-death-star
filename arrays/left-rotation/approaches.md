1. Iterative Shifting
    - Perform d left shifts by taking the first element of the array and moving it to the end of the array, repeated d times
    - Time complexity - O(d * n) - inefficient for large values of d or n
    - Space complexity - O(1) - since we're modifying the array in-place, no additional space is needed

2. Direct Calculation with Slicing
    - Strategy: Instead of shifting one by one, you can directly compute the rotated array by slicing it. For example, for d rotations, split the array into two parts: from index d to the end, and from index 0 to d-1. Concatenate the second part to the first.
    - Time Complexity: O(n) – You only need to traverse the array once to split and combine.
    - Space Complexity: O(n) – This approach creates a new array to store the rotated result.
    - This method is much more efficient as it computes the result in a single pass.

3. In-Place Reversal Approach
    - Strategy: Reverse parts of the array to achieve the desired rotation:
        - Reverse the first d elements.
        - Reverse the remaining n-d elements.
        - Reverse the entire array.
    - Time Complexity: O(n) – Each reversal operation takes linear time.
    - Space Complexity: O(1) – This method modifies the array in place without needing extra space.
    - This is an efficient in-place algorithm that only requires a few reversals of sections of the array, and it avoids the need for auxiliary space.

4. Modulo Indexing
    - Strategy: Use modulo arithmetic to determine the correct position of each element in the rotated array. For each index i, the new index after d rotations can be computed as (i + n - d) % n.
    - Time Complexity: O(n) – You iterate through the array once.
    - Space Complexity: O(n) – You create a new array for the rotated result.
    - This method is efficient, but it requires additional space for the new array.