Given a 6x6 2D array, arr:

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0 
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

An hourglass in A is a subset of values with indices falling in this pattern
in arr's graphical representation:

a b c
  d
e f g

There are 16 hourglasses in arr. An hourglass sum is the sum of an hourglass's 
values. Calculate the hourglass sum for every hourglass in arr, then print 
the maximum hourglass sum. The array will always be 6x6.

Example:
arr = 

-9 -9 -9  1 1 1
 0 -9  0  4 3 2 
-9 -9 -9  1 2 3
 0  0  8  6 6 0
 0  0  0 -2 0 0
 0  0  1  2 4 0

 The 16 hour glass sums are:
 -63, -34, -9, 12, 
-10,   0, 28, 23, 
-27, -11, -2, 10, 
  9,  17, 25, 18

The highest hourglass sum is 28 from the hourglass beginning at row 1, column 2:
0, 4, 3
   1
8, 6, 6

## Function Description

Complete the function hourglassSum.hourglassSum has the following parameter(s):

    int arr[6][6]: an array of integers

Returns

    int: the maximum hourglass sum

Input Format

Each of the 6 lines of inputs contains 6 space-separated integers arr[i][j].

Constraints
Each [i][j] is between -9 to 9
All values of i and j between 0 and 5 (inclusive)

Output Format

Print the largest (maximum) hourglass sum found in arr.
