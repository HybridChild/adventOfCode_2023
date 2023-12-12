import os

# --- Start here ---
scriptDir = os.path.dirname(__file__)
relFilePath = 'example.txt'
absFilePath = os.path.join(scriptDir, relFilePath)

with open(absFilePath) as inputFile:
    inputList = inputFile.read().splitlines()

damageRecords = []
for line in inputList:
    line = line.split(' ')
    line[1] = line[1].split(',')
    damageRecords.append({'whole row': line[0], 'damage groups': [int(num) for num in line[1]]})
