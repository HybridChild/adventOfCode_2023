import os

def find_repeating_pattern(sequence, min_window_size, max_window_size):
    for window_size in range(min_window_size, max_window_size + 1):
        for i in range(len(sequence) - window_size * 2 + 1):
            window1 = sequence[i:i + window_size]
            window2 = sequence[i + window_size:i + 2 * window_size]
            if window1 == window2:
                return {'pattern': window1, 'length': len(window1), 'index': i}  # or return True if you just want to check for repetition without getting the pattern
    return None

def tiltNorth(tileMap):
    for row in range(tileMap['dimensions'][0]):
        for col in range(tileMap['dimensions'][1]):
            if tileMap[str([row, col])] == 'O':
                rolling = True
                tmpRow = row
                while rolling:
                    if tmpRow > 0 and tileMap[str([tmpRow-1, col])] == '.':
                        tileMap[str([tmpRow-1, col])] = 'O'
                        tileMap[str([tmpRow, col])] = '.'
                        tmpRow -= 1
                    else:
                        rolling = False

def tiltSouth(tileMap):
    for row in range(tileMap['dimensions'][0]-1, -1, -1):
        for col in range(tileMap['dimensions'][1]):
            if tileMap[str([row, col])] == 'O':
                rolling = True
                tmpRow = row
                while rolling:
                    if tmpRow < tileMap['dimensions'][0]-1 and tileMap[str([tmpRow+1, col])] == '.':
                        tileMap[str([tmpRow+1, col])] = 'O'
                        tileMap[str([tmpRow, col])] = '.'
                        tmpRow += 1
                    else:
                        rolling = False

def tiltWest(tileMap):
    for col in range(tileMap['dimensions'][1]):
        for row in range(tileMap['dimensions'][0]):
            if tileMap[str([row, col])] == 'O':
                rolling = True
                tmpCol = col
                while rolling:
                    if tmpCol > 0 and tileMap[str([row, tmpCol-1])] == '.':
                        tileMap[str([row, tmpCol-1])] = 'O'
                        tileMap[str([row, tmpCol])] = '.'
                        tmpCol -= 1
                    else:
                        rolling = False

def tiltEast(tileMap):
    for col in range(tileMap['dimensions'][1]-1, -1, -1):
        for row in range(tileMap['dimensions'][0]):
            if tileMap[str([row, col])] == 'O':
                rolling = True
                tmpCol = col
                while rolling:
                    if tmpCol < tileMap['dimensions'][1]-1 and tileMap[str([row, tmpCol+1])] == '.':
                        tileMap[str([row, tmpCol+1])] = 'O'
                        tileMap[str([row, tmpCol])] = '.'
                        tmpCol += 1
                    else:
                        rolling = False

def calculateNorthLoad(tileMap):
    load = 0
    for row in range(tileMap['dimensions'][0]):
        for col in range(tileMap['dimensions'][1]):
            if tileMap[str([row, col])] == 'O':
                load += tileMap['dimensions'][0] - row
    return load

# --- Start here ---
scriptDir = os.path.dirname(__file__)
relFilePath = 'input.txt'
absFilePath = os.path.join(scriptDir, relFilePath)

with open(absFilePath) as inputFile:
    inputList = inputFile.read().splitlines()

# Parse input
tileMap = {'dimensions': [len(inputList), len(inputList[0])]}
for i, line in enumerate(inputList):
    for j, pos in enumerate(line):
        tileMap[str([i, j])] = inputList[i][j]

load = calculateNorthLoad(tileMap)
loadList = [load]

# Part 1
tiltNorth(tileMap)
load = calculateNorthLoad(tileMap)
print('Part 1: ' + str(load))

# Part 2
tiltWest(tileMap)
tiltSouth(tileMap)
tiltEast(tileMap)
load = calculateNorthLoad(tileMap)
loadList.append(load)

for i in range(1, 300):
    tiltNorth(tileMap)
    tiltWest(tileMap)
    tiltSouth(tileMap)
    tiltEast(tileMap)
    load = calculateNorthLoad(tileMap)
    loadList.append(load)

pattern = find_repeating_pattern(loadList, 5, 30)
hump = 1000000000 - pattern['index']
offset = hump % pattern['length']
result = pattern['pattern'][offset]
print('Part 2: ' + str(result))
