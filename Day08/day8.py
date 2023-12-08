import os

# --- Start here ---
scriptDir = os.path.dirname(__file__)
relFilePath = 'input.txt'
absFilePath = os.path.join(scriptDir, relFilePath)

with open(absFilePath) as inputFile:
    inputStr = inputFile.read()

inputList = inputStr.splitlines()

# Parse input
leftRightSequence = list(inputList[0])
networkDict = {}
for i in range(2, len(inputList)):
    networkDict[inputList[i][0:3]] = {'left': inputList[i][7:10], 'right': inputList[i][12:15]}


# Part 1
done = False
nodePosition = 'AAA'
stepCounter = 0
seqIdx = 0
while not done:
    stepCounter += 1
    if leftRightSequence[seqIdx] == 'L':
        nodePosition = networkDict[nodePosition]['left']
    elif leftRightSequence[seqIdx] == 'R':
        nodePosition = networkDict[nodePosition]['right']
    if nodePosition == 'ZZZ':
        done = True
    seqIdx += 1
    if seqIdx >= len(leftRightSequence):
        seqIdx = 0

print('Part 1: ' + str(stepCounter))
