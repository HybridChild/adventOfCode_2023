import os
import re

class EnginePart:
    def __init__(self, lineNumber, number, startPos, endPos):
        self.lineNumber = lineNumber
        self.number = number
        self.startPos = startPos
        self.endPos = endPos
        self.symbol = ''
        self.symbolPos = []


def findNumbersWithPositions(input_string):
    # Define a regular expression pattern to match numbers
    pattern = r'\d+'

    # Use re.finditer to find all occurrences of the pattern in the input string
    matches = re.finditer(pattern, input_string)

    # Create a list to store tuples of (number, start position, end position)
    result = [(match.group(), match.start(), match.end()) for match in matches]

    return result


def scanCircumferenceForSymbol(part, map):
    # Check left
    if part.startPos > 0:
        if map[part.lineNumber][part.startPos - 1] != '.':
            part.symbol = map[part.lineNumber][part.startPos - 1]
            part.symbolPos = [part.lineNumber, part.startPos - 1]
            return
    # Check right
    if part.endPos < len(map[0]):
        if map[part.lineNumber][part.endPos] != '.':
            part.symbol = map[part.lineNumber][part.endPos]
            part.symbolPos = [part.lineNumber, part.endPos]
            return
    # Check top and bottom
    startPos = part.startPos - 1 if part.startPos > 0 else 0
    endPos = part.endPos if part.endPos < len(map[0]) else part.endPos - 1
    for i in range(startPos, endPos + 1):
        if part.lineNumber > 0:
            if map[part.lineNumber - 1][i] != '.':
                part.symbol = map[part.lineNumber - 1][i]
                part.symbolPos = [part.lineNumber - 1, i]
                return
        if part.lineNumber < len(map) - 1:
            if map[part.lineNumber + 1][i] != '.':
                part.symbol = map[part.lineNumber + 1][i]
                part.symbolPos = [part.lineNumber + 1, i]
                return

# --- Start here ---
scriptDir = os.path.dirname(__file__)
relFilePath = 'input.txt'
absFilePath = os.path.join(scriptDir, relFilePath)

with open(absFilePath) as inputFile:
    inputStr = inputFile.read()

engineSchematic = inputStr.splitlines()

# Part 1
enginePartList = []
partSum = 0
for i, line in enumerate(engineSchematic):
    numbersInLine = findNumbersWithPositions(line)
    for number in numbersInLine:
        tmpPart = EnginePart(i, int(number[0]), number[1], number[2])
        scanCircumferenceForSymbol(tmpPart, engineSchematic)
        if tmpPart.symbol != '':
            enginePartList.append(tmpPart)
            partSum += tmpPart.number

print('Part 1: ' + str(partSum))

# Part 2
gearDict = {}
for part in enginePartList:
    if part.symbol == '*':
        if str(part.symbolPos) not in gearDict.keys():
            gearDict[str(part.symbolPos)] = []
        gearDict[str(part.symbolPos)].append(part)

gearRatioSum = 0
for gearKey in gearDict.keys():
    if len(gearDict[gearKey]) == 2:
        gearRatioSum += gearDict[gearKey][0].number * gearDict[gearKey][1].number

print('Part 2: ' + str(gearRatioSum))
