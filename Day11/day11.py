import os

# --- Start here ---
scriptDir = os.path.dirname(__file__)
relFilePath = 'input.txt'
absFilePath = os.path.join(scriptDir, relFilePath)

with open(absFilePath) as inputFile:
    starMap = inputFile.read().splitlines()

for i in range(len(starMap)):
    starMap[i] = list(starMap[i])

# Find galaxy positions
galaxyDict = []
galaxyCounter = 0
for i in range(len(starMap)):
    for j in range(len(starMap[i])):
        if starMap[i][j] == '#':
            galaxyCounter += 1
            galaxyDict.append({'id': galaxyCounter, 'prePos': (i, j), 'postPos': [i, j]})

# Expand universe
for i in range(len(starMap)):
    if '#' not in starMap[i]:
        for galaxy in galaxyDict:
            if galaxy['prePos'][0] > i:
                galaxy['postPos'][0] += 1
for i in range(len(starMap[0])):
    column = [row[i] for row in starMap]
    if '#' not in column:
        for galaxy in galaxyDict:
            if galaxy['prePos'][1] > i:
                galaxy['postPos'][1] += 1

# Find distances
distanceSum = 0
distList = []
for i in range(len(galaxyDict)-1):
    for j in range(i+1, len(galaxyDict)):
        pos1 = galaxyDict[i]['postPos']
        pos2 = galaxyDict[j]['postPos']
        dist = abs(pos2[0]-pos1[0]) + abs(pos2[1]-pos1[1])
        distanceSum += dist
        distList.append({'pair': [galaxyDict[i]['id'], galaxyDict[j]['id']], 'dist': dist})

print('Part 1: ' + str(distanceSum))
