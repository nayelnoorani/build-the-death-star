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
 -63, -34, 
