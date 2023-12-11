import os

# --- Start here ---
scriptDir = os.path.dirname(__file__)
relFilePath = 'example.txt'
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
            galaxyDict.append({'position': [i, j], 'id': galaxyCounter})

# Expand universe
for i in range(len(starMap)):
    if '#' not in starMap[i]:
        for galaxy in galaxyDict:
            if galaxy['position'][0] > i:
                galaxy['position'][0] += 1
for i in range(len(starMap[0])):
    column = [row[i] for row in starMap]
    if '#' not in column:
        for galaxy in galaxyDict:
            if galaxy['position'][1] > i:
                galaxy['position'][1] += 1

# Find distances
distanceSum = 0
distList = []
for i in range(len(galaxyDict)-1):
    for j in range(i+1, len(galaxyDict)):
        pos1 = galaxyDict[i]['position']
        pos2 = galaxyDict[j]['position']
        dist = abs(pos2[0]-pos1[0]) + abs(pos2[1]-pos1[1])
        distList.append({'pair': [galaxyDict[i]['id'], galaxyDict[j]['id']], 'dist': dist})

print('Part 1: ' + str(distanceSum))

# ....1........
# .........2...
# 3............
# .............
# .............
# ........4....
# .5...........
# ............6
# .............
# .............
# .........7...
# 8....9.......

# 1: [ 0, 4]
# 7: [10, 9]
# Between galaxy 1 and galaxy 7: 15

# 3: [2,  0]
# 6: [7, 12]
# Between galaxy 3 and galaxy 6: 17

# 8: [11, 0]
# 9: [11, 5]
# Between galaxy 8 and galaxy 9: 5