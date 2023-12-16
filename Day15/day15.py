import os
import numpy as np

def runHASH(strIn):
    currentValue = np.int16(0)
    for c in strIn:
        currentValue += ord(c)
        currentValue *= 17
        currentValue %= 256
    return currentValue

def insertLens(boxDict, lens):
    if lens['label'] not in boxDict[lens['box']].keys():
        boxDict[lens['box']][lens['label']] = {}
        boxDict[lens['box']][lens['label']]['position'] = boxDict[lens['box']]['lensCnt'] + 1
        boxDict[lens['box']]['lensCnt'] += 1
    boxDict[lens['box']][lens['label']]['focal'] = lens['focal']

def removeLens(boxDict, lens):
    if lens['label'] in boxDict[lens['box']].keys():
        remLens = boxDict[lens['box']].pop(lens['label'])
        boxDict[lens['box']]['lensCnt'] -= 1
        for key in boxDict[lens['box']].keys():
            if key != 'lensCnt':
                if boxDict[lens['box']][key]['position'] > remLens['position']:
                    boxDict[lens['box']][key]['position'] -= 1

def calculateFocusingPower(boxIdx, lensDict):
    focusPowerSum = 0
    for key in lensDict:
        if key != 'lensCnt':
            focusPower = 1
            focusPower *= 1 + boxIdx
            focusPower *= lensDict[key]['position']
            focusPower *= lensDict[key]['focal']
            focusPowerSum += focusPower
    return focusPowerSum


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

# Part 2
for i, step in enumerate(initSeqList):
    stepDict = {}
    actIdx = step.find('-')
    if actIdx == -1:
        actIdx = step.find('=')
        focal = int(step[actIdx+1:])
        stepDict['focal'] = focal
    stepDict['label'] = step[0:actIdx]
    stepDict['box'] = runHASH(stepDict['label'])
    initSeqList[i] = stepDict

boxDict = {}
for i in range(256):
    boxDict[i] = {'lensCnt': 0}

for step in initSeqList:
    if 'focal' in step.keys():
        insertLens(boxDict, step)
    else:
        removeLens(boxDict, step)

focusPowerSum = 0
for box in boxDict:
    focusPowerSum += calculateFocusingPower(box, boxDict[box])

print('Part 2: ' + str(focusPowerSum))
