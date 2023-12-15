import os
import numpy as np

def runHASH(strIn):
    currentValue = np.int16(0)
    for c in strIn:
        currentValue += ord(c)
        currentValue *= 17
        currentValue %= 256
    return currentValue


# --- Start here ---
scriptDir = os.path.dirname(__file__)
relFilePath = 'input.txt'
absFilePath = os.path.join(scriptDir, relFilePath)

with open(absFilePath) as inputFile:
    initSeqList = inputFile.read().split(',')

# Part 1
valueSum = 0
for step in initSeqList:
    valueSum += runHASH(step)

print('Part 1: ' + str(valueSum))
