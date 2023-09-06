def linearSearchV1(x, v):
    index = -1
    for number in range(len(v) + 1):
        if v[number - 1] == x:
            index = number
    return index