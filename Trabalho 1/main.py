from modules.meansure import meansure
from modules.generateVector import generateVector
from algorithms.linearSearchV1 import linearSearchV1

def main():
    archives = [100, 200, 1000, 2000, 5000, 10000, 50000, 100000, 500000, 1000000, 5000000, 10000000, 100000000]
    
    e, m = meansure(linearSearchV1, 50000, generateVector(archives[0], False), 1)

    print(f"Execution time: {e:.10f} seconds")
    print(f"Used memory: {m} bytes\n\n")
    
main()
    
