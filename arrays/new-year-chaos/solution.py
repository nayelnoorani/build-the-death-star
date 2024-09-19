def minimumBribes(q):
    # Write your code here
    bribes = 0

    # Iterate over the queue from right to left
    for i in range(len(q) -1, -1, -1):
        # Check if the person has moved more than 2 positions ahead
        if q[i] - (i + 1) > 2:
            print("Too chaotic")
            return
        
        # Count how many times this person was bribed by checking
        # the positions from max(0, q[i] -2) to the current position
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                bribes += 1

    print(bribes)

q = [1, 2, 5, 3, 7, 8, 6, 4]
minimumBribes(q)