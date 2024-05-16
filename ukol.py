import os

def ukol(path):
    if os.path.exists(path):
        print("Soubor existuje")
    else:
        print("Soubor neexistuje")
    
    with open(path, "r", encoding="utf-8") as f:
        mapka =[list(line) for line in f]
    return mapka




print(ukol("zeroInLine.txt"))
print(ukol("oneInLine.txt"))

#print(ukol("mapka.txt"))