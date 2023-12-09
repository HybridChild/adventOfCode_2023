import os
import re

def find_numbers(input_string):
    # Define a regular expression pattern to match numbers
    pattern = r'-?\d+'

    # Use re.finditer to find all occurrences of the pattern in the input string
    matches = re.finditer(pattern, input_string)

    # Create a list to store tuples of numbers
    result = [(int(match.group())) for match in matches]

    return result


# --- Start here ---
scriptDir = os.path.dirname(__file__)
relFilePath = 'input.txt'
absFilePath = os.path.join(scriptDir, relFilePath)

with open(absFilePath) as inputFile:
    inputStr = inputFile.read()

inputList = inputStr.splitlines()

# Parse input
OASIS_report = []
for line in inputList:
    OASIS_report.append(find_numbers(line))

# Expand data
analysisCollection = []
for line in OASIS_report:
    diffLineList = [line]
    done = False
    while not done:
        diffLine = []
        for i in range(len(diffLineList[-1]) - 1):
            diffLine.append(diffLineList[-1][i+1] - diffLineList[-1][i])
        diffLineList.append(diffLine)
        if diffLine.count(0) == len(diffLine):
            done = True
    analysisCollection.append(diffLineList)

# Calculate history
futureValueSum = 0
pastValueSum = 0
for dataSet in analysisCollection:
    # Part 1
    dataSet[len(dataSet)-1].append(0)
    for i in range(len(dataSet)-2, -1, -1):
        dataSet[i].append(dataSet[i][len(dataSet[i])-1] + dataSet[i+1][len(dataSet[i+1])-1])
    futureValueSum += dataSet[0][len(dataSet[0])-1]

    # Part 2
    dataSet[len(dataSet)-1] = [0] + dataSet[len(dataSet)-1]
    for i in range(len(dataSet)-2, -1, -1):
        dataSet[i] = [dataSet[i][0] - dataSet[i+1][0]] + dataSet[i]
    pastValueSum += dataSet[0][0]


print('Part 1: ' + str(futureValueSum))
print('Part 2: ' + str(pastValueSum))
