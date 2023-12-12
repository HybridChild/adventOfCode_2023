import os
import math

def navigateNetwork(networkDict, nodePosition, dir):
    if dir == 'L':
        nodePosition = networkDict[nodePosition]['left']
    elif dir == 'R':
        nodePosition = networkDict[nodePosition]['right']
    return nodePosition


# --- Start here ---
scriptDir = os.path.dirname(__file__)
relFilePath = 'input.txt'
absFilePath = os.path.join(scriptDir, relFilePath)

with open(absFilePath) as inputFile:
    inputList = inputFile.read().splitlines()

# Parse input
leftRightSequence = list(inputList[0])
networkDict = {}
for i in range(2, len(inputList)):
    networkDict[inputList[i][0:3]] = {'left': inputList[i][7:10], 'right': inputList[i][12:15]}

# Part 2
nodeList = []
for node in networkDict.keys():
    if node[2] == 'A':
        nodeList.append({'node': node})

stepCounter = 0
seqIdx = 0
done = False
while not done:
    stepCounter += 1
    done = True
    for i, node in enumerate(nodeList):
        nodeList[i]['node'] = navigateNetwork(networkDict, node['node'], leftRightSequence[seqIdx])
        if nodeList[i]['node'][2] == 'Z':
            nodeList[i]['Z'] = stepCounter
        if 'Z' not in nodeList[i].keys():
            done = False
    seqIdx += 1
    if seqIdx >= len(leftRightSequence):
        seqIdx = 0

diffList = []
for node in nodeList:
    diffList.append(node['Z'])

# find least common multiple
result = math.lcm(*diffList)

print('Part 2: ' + str(result))
