import os

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


# --- Start here ---
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

coordList = [{'coord': (0, 0), 'enterFrom': 'left'}]
while len(coordList) > 0:
    nextCoord = coordList.pop()
    coordList.extend(lightBeam(mirrorMap, nextCoord['coord'], nextCoord['enterFrom']))

energizedTileCount = 0
for row in range(len(mirrorMap)):
    for col in range(len(mirrorMap[0])):
        if len(mirrorMap[row][col]['enteredFrom']) > 0:
            energizedTileCount += 1

print('Part 1: ' + str(energizedTileCount))
