import os

# --- Start here ---
scriptDir = os.path.dirname(__file__)
relFilePath = 'example.txt'
absFilePath = os.path.join(scriptDir, relFilePath)

with open(absFilePath) as inputFile:
    inputList = inputFile.read().splitlines()

# Parse input
mirrorMapList = []
tmpMap = []
for line in inputList:
    if line == '':
        mirrorMapList.append(tmpMap)
        tmpMap = []
    else:
        tmpMap.append(list(line))
mirrorMapList.append(tmpMap)

# Part 1
def scanHorizontal(map):
    for i in range(1, len(map)):
        if map[i] == map[i-1]:
            


def scanVertical(map):
    pass

horizontal = []
vertical = []
for mirrorMap in mirrorMapList:
    horizontal.append(scanHorizontal(mirrorMap))
    vertical.append(scanVertical(mirrorMap))
    
result = sum(vertical) + 100 * sum(horizontal)