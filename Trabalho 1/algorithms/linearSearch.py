def linearSearchV1(x, v):
    index = -1
    for number in range(len(v)):
        if v[number - 1] == x:
            index = number
    return index

def linearSearchV2(x, v):
    for number in range(len(v)):
        if v[number - 1] == x:
            return number
    return -1