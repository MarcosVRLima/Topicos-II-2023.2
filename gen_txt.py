import os
import random

# Cria uma pasta chamada 'ordenado' se ela não existir
if not os.path.exists('ordenado'):
    os.makedirs('ordenado')

# Cria uma pasta chamada 'desordenado' se ela não existir
if not os.path.exists('desordenado'):
    os.makedirs('desordenado')

# Solicita ao usuário que digite a quantidade de dados a serem gerados
qtd = int(input("Digite a quantidade de dados: "))

# Solicita ao usuário que indique se os dados estarão ordenados ou não
while True:
    ordenado = input("Eles estarão ordenados? (Y/n): ")
    if ordenado == "Y" or ordenado == "n":
        break

vetor = []

# Gera os dados com base na quantidade e na ordenação especificadas pelo usuário
for num in range(1, qtd + 1):  # O loop vai de 1 até qtd (incluindo qtd)
    if ordenado == "Y":
        vetor.append(num)  # Se ordenado for "Y", adiciona os números de 1 a qtd
    else:
        vetor.append(random.randint(1, qtd))  # Se ordenado for "n", adiciona números aleatórios

# Determina em qual pasta os arquivos serão salvos com base na ordenação
pasta = "ordenado" if ordenado == "Y" else "desordenado"

# Define o nome do arquivo, incluindo a quantidade no nome
name = os.path.join(pasta, str(qtd) + ".txt")

# Abre um arquivo chamado "exemplo.txt" em modo de escrita na pasta apropriada
with open(name, "w") as arquivo:
    for i in range(0, len(vetor), 10):  # Itera de 10 em 10 números
        grupo = vetor[i:i+10]  # Pega um grupo de 10 números
        resultado = ", ".join(map(str, grupo))  # Converte para string e junta com vírgula
        arquivo.write(resultado + "\n")  # Escreve no arquivo e adiciona uma quebra de linha

# O arquivo será automaticamente fechado quando o bloco "with" terminar
