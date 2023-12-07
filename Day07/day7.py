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


def handSameTypeGreaterThan(hand1, hand2):
    for i, card in enumerate(hand1['hand']):
        if hand1['hand'][i] != hand2['hand'][i]:
            return hand1['hand'][i] > hand2['hand'][i]


def selectionSort(array):
   # Step through each element of the array
   for startIdx, elem in enumerate(array):
        #  smallestIndex is the index of the smallest element we've encountered so far.
        smallestIdx = startIdx

        # Look for smallest element remaining in the array (starting at startIndex+1)
        for currentIdx in range(startIdx + 1, len(array)):
            # If the current element is smaller than our previously found smallest
            if handSameTypeGreaterThan(array[smallestIdx], array[currentIdx]): # COMPARISON DONE HERE
                # This is the new smallest number for this iteration
                smallestIdx = currentIdx

        # Swap our start element with our smallest element
        array[startIdx], array[smallestIdx] = array[smallestIdx], array[startIdx]


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
relFilePath = 'input.txt'
absFilePath = os.path.join(scriptDir, relFilePath)

with open(absFilePath) as inputFile:
    inputStr = inputFile.read()

inputList = inputStr.splitlines()

# Parse input
handList = []
for line in inputList:
    line = line.split(' ')

    line[0] = ' '.join(line[0])
    line[0] = line[0].replace('T', '10')
    line[0] = line[0].replace('J', '11')
    line[0] = line[0].replace('Q', '12')
    line[0] = line[0].replace('K', '13')
    line[0] = line[0].replace('A', '14')
    line[0] = line[0].split(' ')
    line[0] = [int(num_str) for num_str in line[0]]

    hand = {'hand': line[0], 'bid': int(line[1])}
    hand['type'] = determineHandType(hand['hand'])
    handList.append(hand)

# sort draws
sortedHandList = []
for type in HandType.__members__.values():
    typeDrawList = [hand for hand in handList if hand.get('type') == type]
    selectionSort(typeDrawList)
    sortedHandList = sortedHandList + typeDrawList

totalWinnings = 0
for i, hand in enumerate(sortedHandList):
    sortedHandList[i]['rank'] = i + 1
    totalWinnings += sortedHandList[i]['rank'] * sortedHandList[i]['bid']

print('Part 1: ' + str(totalWinnings))
