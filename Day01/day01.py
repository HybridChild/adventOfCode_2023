import os

# --- Start here ---
scriptDir = os.path.dirname(__file__)
relFilePath = 'input.txt'
absFilePath = os.path.join(scriptDir, relFilePath)

with open(absFilePath) as inputFile:
    inputStr = inputFile.read()

inputList = inputStr.splitlines()

# Part 1 & 2
digitStringList = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
calibrationDigitValueList = []
digitPositionList = []
calibrationDigitStringValueList = []
digitStringPositionList = []

for line in inputList:
    # Part 1
    digit1 = None
    digit2 = None
    scanRightCount = 0
    scanLeftCount = len(line) - 1
    while (digit1 is None or digit2 is None) and scanRightCount < len(line):
        if line[scanRightCount].isdigit() and digit1 is None:
            digit1 = line[scanRightCount]
            digPos1 = scanRightCount
        if line[scanLeftCount].isdigit() and digit2 is None:
            digit2 = line[scanLeftCount]
            digPos2 = scanLeftCount
        scanRightCount += 1
        scanLeftCount -= 1

    calibrationDigitValue = int(digit1 + digit2)
    calibrationDigitValueList.append(calibrationDigitValue)
    digitPositionList.append([digPos1, digPos2])

    # Part 2
    lastIndex = -1
    firstIndex = -1
    for digInt, digitString in enumerate(digitStringList, start=1):
        tmpFirstIdx = line.find(digitString)
        tmpLastIdx = line.rfind(digitString)
        if tmpFirstIdx != -1 and tmpFirstIdx < digPos1:
            digPos1 = tmpFirstIdx
            digit1 = str(digInt)
        if tmpLastIdx != -1 and tmpLastIdx > digPos2:
            digPos2 = tmpLastIdx
            digit2 = str(digInt)

    calibrationDigitStringValue = int(digit1 + digit2)
    calibrationDigitStringValueList.append(calibrationDigitStringValue)
    digitStringPositionList.append([digPos1, digPos2])


print('Part 1: ' + str(sum(calibrationDigitValueList)))
print('Part 2: ' + str(sum(calibrationDigitStringValueList)))
