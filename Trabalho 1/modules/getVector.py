def getVector(quantity, ordened):
    vector = []
    name = "data/ordened/" if ordened == True else "data/unordened/"
    name = name + str(quantity) + ".txt"
    # Abra o arquivo em modo de leitura
    with open(name, "r") as archive:
        # Leia o conteúdo do arquivo linha por linha
        lines = archive.readlines()
        
        # Itere sobre as linhas
        for line in lines:
            # Divida a linha em números usando vírgulas como separadores
            numbers = line.strip().split(",")  # Use split(" ") se os números estiverem separados por espaços
            
            # Converta os números de strings para inteiros e adicione-os ao vetor
            vector.extend(map(int, numbers))
        
    return vector

# print(vetor(100, "S"))