def minimumBribes(q):
    # Write your code here
    bribes = 0
    if q == sorted(q):
        pass
    else:
        for i, person in enumerate(q):
            if person - i > 3:
                print("Too chaotic")
                return None
            elif person - i > 1:
                bribes += person - (i + 1)
    print(bribes)