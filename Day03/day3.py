import os
import re


class EnginePart:
    def __init__(self, line, num, startPos, endPos):
        self.line = line
        self.number = num
        self.startPos = startPos
        self.endPos = endPos
        self.symbol = ''
    

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
        if map[part.line][part.startPos - 1] != '.':
            part.symbol = map[part.line][part.startPos - 1]
            return
    # Check right
    if part.endPos < len(map[0]):
        if map[part.line][part.endPos] != '.':
            part.symbol = map[part.line][part.endPos]
            return
    # Check top and bottom
    startPos = part.startPos - 1 if part.startPos > 0 else 0
    endPos = part.endPos if part.endPos < len(map[0]) else part.endPos - 1
    for i in range(startPos, endPos + 1):
        if part.line > 0:
            if map[part.line - 1][i] != '.':
                part.symbol = map[part.line - 1][i]
                return
        if part.line < len(map) - 1:
            if map[part.line + 1][i] != '.':
                part.symbol = map[part.line + 1][i]
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
