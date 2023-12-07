import os
from enum import Enum

class HandType(Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented
    def __gt__(self, other):
        if self.__class__ is other.__class__:
            return self.value > other.value
        return NotImplemented
    def __eq__(self, other):
        if self.__class__ is other.__class__:
            return self.value == other.value
        return NotImplemented
    def __ne__(self, other):
        if self.__class__ is other.__class__:
            return self.value != other.value
        return NotImplemented

def determineHandType(hand):
    counterDict = {}
    for card in hand:
        if card not in counterDict.keys():
            counterDict[card] = 1
        else:
            counterDict[card] += 1
    
    if 5 in counterDict.values():
        return HandType.FIVE_OF_A_KIND
    if 4 in counterDict.values():
        return HandType.FOUR_OF_A_KIND
    if 3 in counterDict.values() and 2 in counterDict.values():
        return HandType.FULL_HOUSE
    if 3 in counterDict.values():
        return HandType.THREE_OF_A_KIND
    if list(counterDict.values()).count(2) == 2:
        return HandType.TWO_PAIR
    if 2 in counterDict.values():
        return HandType.ONE_PAIR
    return HandType.HIGH_CARD


# --- Start here ---
scriptDir = os.path.dirname(__file__)
relFilePath = 'example.txt'
absFilePath = os.path.join(scriptDir, relFilePath)

with open(absFilePath) as inputFile:
    inputStr = inputFile.read()

inputList = inputStr.splitlines()

# Parse input
handList = []
for line in inputList:
    line = line.split(' ')
    draw = {'bid': int(line[1]), 'hand': line[0]}
    draw['type'] = determineHandType(draw['hand'])
    handList.append(draw)
