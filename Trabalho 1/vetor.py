def vetor(qtd, ordenado):
    v = []
    nome = "ordenado/" if ordenado == True else "desordenado/"
    nome = nome + str(qtd) + ".txt"
    # Abra o arquivo em modo de leitura
    with open(nome, "r") as arquivo:
        # Leia o conteúdo do arquivo linha por linha
        linhas = arquivo.readlines()
        
        # Itere sobre as linhas
        for linha in linhas:
            # Divida a linha em números usando vírgulas como separadores
            numeros = linha.strip().split(",")  # Use split(" ") se os números estiverem separados por espaços
            
            # Converta os números de strings para inteiros e adicione-os ao vetor
            v.extend(map(int, numeros))
        
    return v

# print(vetor(100, "S"))