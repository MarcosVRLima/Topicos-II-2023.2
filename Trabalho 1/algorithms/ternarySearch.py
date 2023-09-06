def ternarySearch(x, v, n):
    start = 0
    end = n - 1
    
    while start <= end:
        leftMid = start + int((end - start) / 3)
        rightMid = end + int((end - start) / 3)
        
        if leftMid == x:
            return leftMid
        elif rightMid == x:
            return rightMid
        elif leftMid > x:
            end = leftMid - 1
        elif rightMid < x:
            start = rightMid + 1
        else:
            start = leftMid + 1
            end = rightMid - 1
    
    return -1