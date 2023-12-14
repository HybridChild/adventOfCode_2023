import os

def tiltNorth(tileMap):
    for row in range(tileMap['dimensions'][0]):
        for col in range(tileMap['dimensions'][1]):
            if tileMap[str([row, col])] == 'O':
                rolling = True
                tmpRow = row
                while rolling:
                    if tmpRow > 0 and tileMap[str([tmpRow-1, col])] == '.':
                        tileMap[str([tmpRow-1, col])] = 'O'
                        tileMap[str([tmpRow, col])] = '.'
                        tmpRow -= 1
                    else:
                        rolling = False

def calculateNorthLoad(tileMap):
    load = 0
    for row in range(tileMap['dimensions'][0]):
        for col in range(tileMap['dimensions'][1]):
            if tileMap[str([row, col])] == 'O':
                load += tileMap['dimensions'][0] - row
    return load

# --- Start here ---
scriptDir = os.path.dirname(__file__)
relFilePath = 'input.txt'
absFilePath = os.path.join(scriptDir, relFilePath)

with open(absFilePath) as inputFile:
    inputList = inputFile.read().splitlines()

# Parse input
tileMap = {'dimensions': [len(inputList), len(inputList[0])]}
for i, line in enumerate(inputList):
    for j, pos in enumerate(line):
        tileMap[str([i, j])] = inputList[i][j]

# Part 1
tiltNorth(tileMap)
load = calculateNorthLoad(tileMap)
print('Part 1: ' + str(load))
