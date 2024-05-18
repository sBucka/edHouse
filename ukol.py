import os

def is_not_num_dot(char):
    return not char.isdigit() and char != '.'

def is_valid_num(mapka, line, char):
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di == dj == 0:
                continue
            ni, nj = line + di, char + dj
            if 0 <= ni < len(mapka) and 0 <= nj < len(mapka[line]) and is_not_num_dot(mapka[ni][nj]):
                return True
    return False

def ukol(file):
    inNum = False
    validNum = False
    #myValidNumbers = []
    number = ""
    mySum = 0
    with open(file, "r") as f:
        mapka = [list(line.strip()) for line in f.readlines()]
        for i in range(len(mapka)):
            for j in range(len(mapka[i])):
                if mapka[i][j].isdigit():
                    inNum = True
                    number += mapka[i][j]
                    if is_valid_num(mapka, i, j):
                        validNum = True
                else:
                    if inNum:
                        if validNum:
                            number = int(number)
                            mySum += number
                            #myValidNumbers.append(number)
                        number = ""
                        inNum = False
                        validNum = False
    if inNum and validNum:
        number = int(number)
        #myValidNumbers.append(number)
        mySum += number
    return mySum
    



print(ukol("example.txt"))
print(ukol("mapka.txt"))