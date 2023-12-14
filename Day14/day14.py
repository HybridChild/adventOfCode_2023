import os
import copy

# --- Start here ---
scriptDir = os.path.dirname(__file__)
relFilePath = 'input.txt'
absFilePath = os.path.join(scriptDir, relFilePath)

with open(absFilePath) as inputFile:
    inputList = inputFile.read().splitlines()

# Parse input
rockList = []
tileMap = {}
for i, line in enumerate(inputList):
    for j, pos in enumerate(line):
        tileMap[str([i, j])] = inputList[i][j]
        if inputList[i][j] != '.':
            rockList.append({'type': inputList[i][j], 'pos': [i, j]})

# Tilt north
for i, rock in enumerate(rockList):
    rock = copy.deepcopy(rockList[i])
    if rock['type'] == 'O':
        rolling = True
        while rolling:
            if rock['pos'][0] > 0 and tileMap[str([rock['pos'][0]-1, rock['pos'][1]])] == '.':
                tileMap[str([rock['pos'][0]-1, rock['pos'][1]])] = 'O'
                tileMap[str([rock['pos'][0], rock['pos'][1]])] = '.'
                rockList[i]['pos'][0] -= 1
                rock['pos'][0] -= 1
            else:
                rolling = False

# Calculate load
load = 0
for rock in rockList:
    if rock['type'] == 'O':
        load += len(inputList) - rock['pos'][0]

# Part 1
print('Part 1: ' + str(load))
