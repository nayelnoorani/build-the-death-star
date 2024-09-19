def rotLeft(a, d):
    n = len(a)
    d = d%n # in case d is larger than n
    rotated_array = [0] * n

    for i in range(n):
        rotated_array[i] = a[(i + d) % n]

    return rotated_array