import time, tracemalloc, random
from numpy import mean

from modules.getVector import getVector
from modules.report import report

def meansure(algorithms, archives, iterations = 1):
    qtdAlgorithms = len(algorithms)
    qtdArchives = len(archives) - 1 
    
    for i in range(qtdAlgorithms):
        for j in range(qtdArchives * 2):
            quantity = archives[j % qtdArchives]
            numberSearched = 5
            ordened = True if j >= qtdArchives else False
            vector = getVector(quantity, ordened)
            acepted = False
            
            if i == 0:
                if ordened == True:
                    executionTime, usedMemory = run(algorithms[i], numberSearched, vector, iterations, True)
                    acepted = True
            elif i == 1:
                if ordened == True:
                    executionTime, usedMemory = run(algorithms[i], numberSearched, vector, iterations)
                    acepted = True
            else:
                executionTime, usedMemory = run(algorithms[i], numberSearched, vector, iterations)
                acepted = True
                
            del vector
            
            if acepted == True:   
                data = {
                    "algorithm": algorithms[i].__name__,
                    "iterations": iterations,
                    "quantity": quantity,
                    "ordened": ordened,
                    "numberSearched": numberSearched,
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
        if binarySearch == True:
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
        