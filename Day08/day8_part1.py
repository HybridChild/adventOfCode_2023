import os

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

# Part 1
nodePosition = 'AAA'
stepCounter = 0
seqIdx = 0
done = False
while not done:
    stepCounter += 1
    nodePosition = navigateNetwork(networkDict, nodePosition, leftRightSequence[seqIdx])
    if nodePosition == 'ZZZ':
        done = True
    seqIdx += 1
    if seqIdx >= len(leftRightSequence):
        seqIdx = 0

print('Part 1: ' + str(stepCounter))
