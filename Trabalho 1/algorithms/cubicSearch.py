def cubicSearch(x, v):
    position = -1
    
    for i in range(len(v)):
        for j in range(len(v)):
            for k in range(len(v)):
                if v[i] == x and v[j] == x and v[k] == x:
                    position = i
                    
    return position