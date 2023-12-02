import os
import re

# --- Start here ---
scriptDir = os.path.dirname(__file__)
relFilePath = 'input.txt'
absFilePath = os.path.join(scriptDir, relFilePath)

with open(absFilePath) as inputFile:
    inputStr = inputFile.read()

inputList = inputStr.splitlines()

# Parse input
gameList = []
for gameStr in inputList:
    gameStr = gameStr[gameStr.find(':') + 1:]
    pullStrList = gameStr.split(';')
    
    digitPattern = r'\d+'
    translation_table = str.maketrans('', '', ' 0123456789')
    pullList = []
    for pullStr in pullStrList:
        cubeStrList = pullStr.split(',')
        cubeDict = {}
        for cubeStr in cubeStrList:
            amountStr = re.findall(digitPattern, cubeStr)[0]
            amount = int(amountStr)
            color = cubeStr.translate(translation_table)
            cubeDict[color] = amount
        pullList.append(cubeDict)
    gameList.append(pullList)

# Part 1 and 2
ifBag = {'red': 12, 'green': 13, 'blue': 14}

possibleGameIndexes = []
minimumGamePowerList = []
for i, game in enumerate(gameList, start=1):
    gameIsPossible = True
    minimumCubeDict = {'red': 0, 'green': 0, 'blue': 0}
    for draw in game:
        for color in draw:
            if draw[color] > ifBag[color]:
                gameIsPossible = False
                #break
            if draw[color] > minimumCubeDict[color]:
                minimumCubeDict[color] = draw[color]
        # if not gameIsPossible:
        #     break
    if gameIsPossible:
        possibleGameIndexes.append(i)
    minimumGamePowerList.append(minimumCubeDict['red'] * minimumCubeDict['green'] * minimumCubeDict['blue'])

print('Part 1: ' + str(sum(possibleGameIndexes)))
print('Part 2: ' + str(sum(minimumGamePowerList)))
