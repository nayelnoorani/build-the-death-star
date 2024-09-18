1. Brute Force:
   - Iterating through every possible starting point of an hourglass in the 6x6 array
   - For each starting point, manually extracting the 7 values from that hourglass
   - Calculating the sum of the 7 values
   - Keeping track of the maximum hourglass sum encountered
   - Returning the maximum sum at the end

2. Sliding Window Technique
  - Define a window that captures the hourglass shape (3x3 with the side values in the middle row removed)
  - Slide the window row by row and column by column
  - At each position, sum the values inside the window
  - Keep track of the maximum sum encountered
  - Return the maximum sum at the end
  
  %% in this particular case, the code for both options above looks exactly the same

3. Dynamic Programming Approach
  - Precompute partial sums: create a table where each entry stores the sum of all elements from the top
  left corner (0,0) of the array up to that entry (inclusive). This is a prefix sum array.
  - use precomputed sums to calculate hourglass sums: 
  - reuse overlapping sums
  - iterate efficiently

  %% Reduces redundant calculations by not recalculating the same sums multiple times. Performance difference
  for a 6x6 grid is minimal but concept becomes more valuable for larger grids