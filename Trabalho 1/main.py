from modules.meansure import meansure

from algorithms.linearSearch import linearSearchV1, linearSearchV2
from algorithms.quadraticSearch import quadraticSearch
from algorithms.cubicSearch import cubicSearch
from algorithms.binarySearch import binarySearch
from algorithms.ternarySearch import ternarySearch


def main():
    archives = [100, 200, 1000, 2000, 5000, 10000, 50000, 100000, 500000, 1000000, 5000000, 10000000, 100000000]
    algorithms = [binarySearch, ternarySearch, linearSearchV1, linearSearchV2, quadraticSearch, cubicSearch]
    iterations = 1
    
    meansure(algorithms, archives, iterations)
    
main()
    
