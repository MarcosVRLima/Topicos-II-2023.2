import time, tracemalloc, random
from numpy import mean

from modules.getVector import getVector
from modules.report import report

def meansure(algorithms, archives, iterations = 1):
    qtdAlgorithms = len(algorithms)
    qtdArchives = len(archives) - 1 
    
    for i in range(qtdAlgorithms):
        numberSearched = random.randint(1, archives[qtdArchives])
        for j in range(qtdArchives):
            #print((j % (len(archives) - 1)))
            string = "ordenados"
            vector = getVector(archives[j], False)
            if i != 0:
                executionTime, usedMemory = run(algorithms[i], numberSearched, vector, iterations, True)
            else:
                executionTime, usedMemory = run(algorithms[i], numberSearched, vector, iterations)
                
            data = {
                "algorithm": algorithms[i].__name__,
                "quantity": archives[j],
                "ordened": string,
                "executionTime": executionTime,
                "usedMemory": usedMemory
            }
            
            report(data)

def run(algorithm, x, v, repeat = 1, binarySearch = False):            
    memoryPeaks = []
    timeExecutions = []
    for _ in range(repeat):
        tracemalloc.start()
        
        startTime = time.time()
        if binarySearch:
            algorithm(x, v, 0, len(v))
        else:
            algorithm(x, v)
       
        endTime = time.time()
        
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        executionTime = endTime - startTime
        
        timeExecutions.append(executionTime)
        memoryPeaks.append(peak)
        
    return [mean(timeExecutions), int(mean(memoryPeaks))]
        