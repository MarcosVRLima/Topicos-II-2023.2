import time, tracemalloc
import numpy as np

def meansure(algorithm, x, v, repeat = 1):
    memoryPeaks = []
    timeExecutions = []
    for _ in range(repeat):
        tracemalloc.start()
        
        startTime = time.time()
        
        algorithm(x, v)
       
        endTime = time.time()
        
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        executionTime = endTime - startTime
        
        timeExecutions.append(executionTime)
        memoryPeaks.append(peak)
        
    return [np.mean(timeExecutions), int(np.mean(memoryPeaks))]
        