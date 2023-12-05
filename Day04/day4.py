import os
import re

def find_numbers(input_string):
    # Define a regular expression pattern to match numbers
    pattern = r'\d+'

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
cardPile = []
for cardStr in inputList:    
    cardStr = cardStr[cardStr.find(':') + 1:]
    cardStr = cardStr.split('|')

    winNum = find_numbers(cardStr[0])
    myNum = find_numbers(cardStr[1])
    card = {'winNumbers': winNum, 'myNumbers': myNum, 'worth': 0, 'copies': 1}

    cardPile.append(card)

# Part 1
totalPoints = 0
totalCardCount = 0
for i, card in enumerate(cardPile):
    cardWorth = 0
    winCnt = 0
    for myNum in card['myNumbers']:
        if myNum in card['winNumbers']:
            winCnt += 1
            if cardWorth == 0:
                cardWorth = 1
            else:
                cardWorth = cardWorth * 2
    cardPile[i]['worth'] = cardWorth

    for j in range(i+1, i+1+winCnt):
        if j < len(cardPile):
            cardPile[j]['copies'] += card['copies']

    totalPoints += cardWorth
    totalCardCount += card['copies']

print('Part 1: ' + str(totalPoints))
print('Part 2: ' + str(totalCardCount))
