import os

def report(data):
    if not os.path.exists('data/reports/ordened'):
        os.makedirs('data/reports/ordened')
        
    if not os.path.exists('data/reports/unordened'):
        os.makedirs('data/reports/unordened')
        
    string = "ordened/" if data['ordened'] == True else "unordened"
    archiveName = 'data/reports/' + string + "-" + data["algorithm"] + "-" + str(data["quantity"]) + '-searchedNumber-' + str(data["numberSearched"]) + ".txt"
    
    response = [
        "Algorithm: " + data["algorithm"],
        "Quantity of entries: " + str(data["quantity"]),
        "Number searched: " + str(data["numberSearched"]),
        "Ordened? " + str(data["ordened"]),
        "Iterations: " + str(data["iterations"]),
        "Execution time: " + str(data["executionTime"]) + " Seconds" ,
        "Used memory: " + str(data["usedMemory"]) + " B"
    ]
    
    with open (archiveName, 'w') as arquivo:
        for line in response:
            arquivo.write(line + "\n")
            
    print(data)