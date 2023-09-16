def ternarySearch(x, v):
    start = 0
    end = len(v) - 1
    
    while start <= end:
        leftMid = start + int((end - start) / 3)
        rightMid = end - int((end - start) / 3)
        
        if v[leftMid] == x:
            return leftMid
        elif v[rightMid] == x:
            return rightMid
        elif v[leftMid] > x:
            end = leftMid - 1
        elif v[rightMid] < x:
            start = rightMid + 1
        else:
            start = leftMid + 1
            end = rightMid - 1
    
    return -1