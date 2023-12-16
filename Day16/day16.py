import os
import copy
import time

def lightBeam(mirrorMap, coord, enterFrom):
    if enterFrom in mirrorMap[coord[0]][coord[1]]['enteredFrom']:
        return []
    else:
        mirrorMap[coord[0]][coord[1]]['enteredFrom'].append(enterFrom)

    nextCoords = []

    if mirrorMap[coord[0]][coord[1]]['symbol'] == '.':
        if enterFrom == 'bottom' and coord[0] > 0:
            nextCoords.append({'coord': [coord[0] - 1, coord[1]], 'enterFrom': 'bottom'})
        elif enterFrom == 'top' and coord[0] < len(mirrorMap) - 1:
            nextCoords.append({'coord': [coord[0] + 1, coord[1]], 'enterFrom': 'top'})
        elif enterFrom == 'right' and coord[1] > 0:
            nextCoords.append({'coord': [coord[0], coord[1] - 1], 'enterFrom': 'right'})
        elif enterFrom == 'left' and coord[1] < len(mirrorMap[coord[0]]) - 1:
            nextCoords.append({'coord': [coord[0], coord[1] + 1], 'enterFrom': 'left'})
    elif mirrorMap[coord[0]][coord[1]]['symbol'] == '/':
        if enterFrom == 'bottom' and coord[1] < len(mirrorMap[coord[0]]) - 1:
            nextCoords.append({'coord': [coord[0], coord[1] + 1], 'enterFrom': 'left'})
        elif enterFrom == 'top' and coord[1] > 0:
            nextCoords.append({'coord': [coord[0], coord[1] - 1], 'enterFrom': 'right'})
        elif enterFrom == 'right' and coord[0] < len(mirrorMap) - 1:
            nextCoords.append({'coord': [coord[0] + 1, coord[1]], 'enterFrom': 'top'})
        elif enterFrom == 'left' and coord[0] > 0:
            nextCoords.append({'coord': [coord[0] - 1, coord[1]], 'enterFrom': 'bottom'})
    elif mirrorMap[coord[0]][coord[1]]['symbol'] == '\\':
        if enterFrom == 'bottom' and coord[1] > 0:
            nextCoords.append({'coord': [coord[0], coord[1] - 1], 'enterFrom': 'right'})
        elif enterFrom == 'top' and coord[1] < len(mirrorMap[coord[0]]) - 1:
            nextCoords.append({'coord': [coord[0], coord[1] + 1], 'enterFrom': 'left'})
        elif enterFrom == 'right' and coord[0] > 0:
            nextCoords.append({'coord': [coord[0] - 1, coord[1]], 'enterFrom': 'bottom'})
        elif enterFrom == 'left' and coord[0] < len(mirrorMap) - 1:
            nextCoords.append({'coord': [coord[0] + 1, coord[1]], 'enterFrom': 'top'})
    elif mirrorMap[coord[0]][coord[1]]['symbol'] == '-':
        if enterFrom == 'bottom' or enterFrom == 'top':
            if coord[1] > 0:
                nextCoords.append({'coord': [coord[0], coord[1] - 1], 'enterFrom': 'right'})
            if coord[1] < len(mirrorMap[coord[0]]) - 1:
                nextCoords.append({'coord': [coord[0], coord[1] + 1], 'enterFrom': 'left'})
        elif enterFrom == 'right' and coord[1] > 0:
            nextCoords.append({'coord': [coord[0], coord[1] - 1], 'enterFrom': 'right'})
        elif enterFrom == 'left' and coord[1] < len(mirrorMap[coord[0]]) - 1:
            nextCoords.append({'coord': [coord[0], coord[1] + 1], 'enterFrom': 'left'})
    elif mirrorMap[coord[0]][coord[1]]['symbol'] == '|':
        if enterFrom == 'left' or enterFrom == 'right':
            if coord[0] > 0:
                nextCoords.append({'coord': [coord[0] - 1, coord[1]], 'enterFrom': 'bottom'})
            if coord[0] < len(mirrorMap) - 1:
                nextCoords.append({'coord': [coord[0] + 1, coord[1]], 'enterFrom': 'top'})
        elif enterFrom == 'bottom' and coord[0] > 0:
            nextCoords.append({'coord': [coord[0] - 1, coord[1]], 'enterFrom': 'bottom'})
        elif enterFrom == 'top' and coord[0] < len(mirrorMap) - 1:
            nextCoords.append({'coord': [coord[0] + 1, coord[1]], 'enterFrom': 'top'})

    return nextCoords

def shineLightBeam(mirrorMap, startCoord):
    coordList = [startCoord]
    while len(coordList) > 0:
        nextCoord = coordList.pop()
        coordList.extend(lightBeam(mirrorMap, nextCoord['coord'], nextCoord['enterFrom']))

def countEnergized(mirrorMap):
    energizedTileCount = 0
    for row in range(len(mirrorMap)):
        for col in range(len(mirrorMap[0])):
            if len(mirrorMap[row][col]['enteredFrom']) > 0:
                energizedTileCount += 1
    return energizedTileCount


# --- Start here ---
start_time = time.time()

scriptDir = os.path.dirname(__file__)
relFilePath = 'input.txt'
absFilePath = os.path.join(scriptDir, relFilePath)

with open(absFilePath) as inputFile:
    mirrorMap = [list(row) for row in inputFile.read().splitlines()]

for row in range(len(mirrorMap)):
    for col in range(len(mirrorMap[0])):
        mirrorMap[row][col] = {'coordinate': (row, col), \
                               'symbol': mirrorMap[row][col], \
                               'enteredFrom': []}

coordList = []
for row in range(len(mirrorMap)):
    coordList.append({'coord': (row, 0), 'enterFrom': 'left'})
    coordList.append({'coord': (row, len(mirrorMap[row]) - 1), 'enterFrom': 'right'})

for col in range(len(mirrorMap[0])):
    coordList.append({'coord': (0, col), 'enterFrom': 'top'})
    coordList.append({'coord': (len(mirrorMap) - 1, col), 'enterFrom': 'bottom'})

energizedDict = {}
for startCoord in coordList:
    mirrorMapCopy = copy.deepcopy(mirrorMap)
    shineLightBeam(mirrorMapCopy, startCoord)
    energizedDict[str(startCoord['coord']) + startCoord['enterFrom']] = countEnergized(mirrorMapCopy)

maxEnergized = 0
for key in energizedDict.keys():
    if energizedDict[key] > maxEnergized:
        maxEnergized = energizedDict[key]

print('Part 1: ' + str(energizedDict['(0, 0)left']))
print('Part 2: ' + str(maxEnergized))

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")
