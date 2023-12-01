import os

# --- Start here ---
scriptDir = os.path.dirname(__file__)
relFilePath = 'input.txt'
absFilePath = os.path.join(scriptDir, relFilePath)

with open(absFilePath) as inputFile:
    inputStr = inputFile.read()

inputList = inputStr.splitlines()

# Part 1
calibrationValueList = []

for line in inputList:
    digit1 = None
    digit2 = None
    scanRightCount = 0
    scanLeftCount = len(line) - 1
    while digit1 is None or digit2 is None:
        if line[scanRightCount].isdigit() and digit1 is None:
            digit1 = line[scanRightCount]
        if line[scanLeftCount].isdigit() and digit2 is None:
            digit2 = line[scanLeftCount]
        scanRightCount += 1
        scanLeftCount -= 1

    calibrationValue = int(digit1 + digit2)
    calibrationValueList.append(calibrationValue)

print(sum(calibrationValueList))
