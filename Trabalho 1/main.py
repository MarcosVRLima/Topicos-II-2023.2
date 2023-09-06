from modules.meansure import meansure
from modules.generateVector import generateVector

from algorithms.linearSearch import linearSearchV1, linearSearchV2
from algorithms.quadraticSearch import quadraticSearch
from algorithms.cubicSearch import cubicSearch
from algorithms.binarySearch import binarySearch
from algorithms.ternarySearch import ternarySearch


def main():
    archives = [100, 200, 1000, 2000, 5000, 10000, 50000, 100000, 500000, 1000000, 5000000, 10000000, 100000000]
    
    e, m = meansure(linearSearchV1, 50000, generateVector(archives[0], True), 1)

    print(f"Execution time: {e:.10f} seconds")
    print(f"Used memory: {m} bytes")
    
    #b = binarySearch(50000, generateVector(archives[7], True), 0, archives[7])
    #print(f"{b}")
    
    #t = ternarySearch(50, generateVector(archives[6], False), archives[6])
    #print(f"{t}")
    
main()
    
