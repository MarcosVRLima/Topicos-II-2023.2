import time, os, psutil
from vetor import vetor
import numpy as np

from buscalinearv1 import buscaLinearV1

# Função para obter o uso de memória atual
def get_memory_usage():
    pid = os.getpid()
    process = psutil.Process(pid)
    memory_info = process.memory_full_info()
    return memory_info.rss 

def meansure(algoritmo, x, v):
    while True:
        initial_memory_usage = get_memory_usage()
        startTime = time.time()
        
        indice = algoritmo(x, v)
        
        endTime = time.time()
        final_memory_usage = get_memory_usage()
        
        executionTime = endTime - startTime
        memoryUsage = final_memory_usage - initial_memory_usage
        
        if memoryUsage > 0:
            return [executionTime, memoryUsage]
        
def main():
    arquivos = [100, 200, 1000, 2000, 5000, 10000, 50000, 100000, 500000, 1000000, 5000000, 10000000]
    numberSearch = 50000
    
    e, m = meansure(buscaLinearV1, numberSearch, vetor(arquivos[9], True))

    print(f"Tempo de execução: {e} s")
    print(f"Memoria utilizada: {m} B\n\n")
    
main()
    
