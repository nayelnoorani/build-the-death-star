'''
Given a stream of numbers, select a random number from the stream with equal probability and O(1) space in selection. 

Input:
def random_number(x, y=0, count=1):
    pass

x is the new value from the stream
y is the previously selected value
count is the size of the stream


Approaches to select a random element:

Reservoir Sampling (Single Item):
Use a simple reservoir sampling algorithm that maintains one random number from the stream with equal probability.
This is implemented below.

Iterative Probability Adjustment:
Adjust the probability of selecting the new element at each step based on the number of elements seen so far.

Modulo-Based Selection:
Use a modulo operation on the count of stream elements to decide when to replace the selected value.

Random Index Selection:
Generate a random index at each step and replace the selected number if the new element matches that index.

'''

import random

def random_number(x, y=0, count=1):
    # Select the first number in the reservoir
    if count == 1:
        y = x
    else:
        # Generate a random number between 1 and count (inclusive)
        rand_idx = random.randint(1, count)
        # Replace y with the new element if the random number is 1
        if rand_idx == 1:
            y = x

    return y

# Simulating a stream of numbers
stream = [4, 7, 3, 2, 5, 9, 8, 6, 1, 0]
selected_value = 0

for i, num in enumerate(stream):
    selected_value = random_number(num, selected_value, i + 1)
    print(f"After processing {i+1} numbers, selected value is: {selected_value}")