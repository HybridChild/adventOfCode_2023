import os

# --- Start here ---
scriptDir = os.path.dirname(__file__)
relFilePath = 'input.txt'
absFilePath = os.path.join(scriptDir, relFilePath)

with open(absFilePath) as inputFile:
    digPlans = inputFile.read().splitlines()

mapSize = [1, 1]
xPos = 1
yPos = 1
for i, line in enumerate(digPlans):
    line = line.split(' ')
    line[2] = line[2][1:len(line[2])-1]
    digPlans[i] = {'dir': line[0], 'val': int(line[1]), 'code': line[2]}
    if digPlans[i]['dir'] == 'R':
        xPos += digPlans[i]['val']
        if xPos > mapSize[0]:
            mapSize[0] = xPos
    if digPlans[i]['dir'] == 'L':
        xPos -= digPlans[i]['val']
    if digPlans[i]['dir'] == 'D':
        yPos += digPlans[i]['val']
        if yPos > mapSize[1]:
            mapSize[1] = yPos
    if digPlans[i]['dir'] == 'U':
        yPos -= digPlans[i]['val']
    assert(xPos > 0)
    assert(yPos > 0)

tileMap = [['.' for _ in range(mapSize[0])] for _ in range(mapSize[1])]
