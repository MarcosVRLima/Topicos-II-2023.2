def quadraticSearch(x, v):
    count = 0
    position = -1
    entered = False
    
    for i in range(len(v)):
        for j in range(len(v)):
            if v[i] == x and entered == False:
                position = i
                
                if v[j] == x:
                    count += 1

        if count > 0:
            entered = True
    
    return [position, count]
                
    