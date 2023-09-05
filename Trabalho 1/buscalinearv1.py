def buscaLinearV1(x, v):
    indice = -1
    for num in range(1, len(v) + 1):
        if v[num-1] == x:
            indice = num
    return indice
      
#buscaLinearV1(500000, vetor(5000000, "n"))