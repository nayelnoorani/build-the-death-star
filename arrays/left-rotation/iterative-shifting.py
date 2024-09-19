def rotLeft (a, d):

    for _ in range(d):
        first = a.pop(0)
        a.append(first)

    return a