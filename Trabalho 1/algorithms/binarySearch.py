def binarySearch(x, v, e, d):
    mid = int((e + d) / 2)
    
    if mid == x:
        return mid
    
    if e >= d:
        return -1
    elif v[mid] < x:
        binarySearch(x, v, mid + 1, d)
    else:
        binarySearch(x, v, e, mid - 1)
    
        