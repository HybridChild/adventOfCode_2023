import os
import copy
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


def determineHandType1(hand):
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


def determineHandType2(hand):
    # Five of a kind, where all five cards have the same label: AAAAA
    # Four of a kind, where four cards have the same label and one card has a different label: AA8AA
    # Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
    # Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
    # Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
    # One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
    # High card, where all cards' labels are distinct: 23456
    
    counterDict = {}
    for card in hand:
        if card not in counterDict.keys():
            counterDict[card] = 1
        else:
            counterDict[card] += 1
    
    if 1 in counterDict.keys():
        tmpJ = counterDict[1]
        counterDict[1] = 0
        max_key = max(counterDict, key=counterDict.get)
        counterDict[max_key] += tmpJ

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


def makeHandDictType1(handStr):
    tmpHand = copy.deepcopy(handStr)
    tmpHand = tmpHand.split(' ')
    tmpHand[0] = ' '.join(tmpHand[0])
    tmpHand[0] = tmpHand[0].replace('T', '10')
    tmpHand[0] = tmpHand[0].replace('J', '11')
    tmpHand[0] = tmpHand[0].replace('Q', '12')
    tmpHand[0] = tmpHand[0].replace('K', '13')
    tmpHand[0] = tmpHand[0].replace('A', '14')
    tmpHand[0] = tmpHand[0].split(' ')
    tmpHand[0] = [int(num_str) for num_str in tmpHand[0]]

    newHand = {'hand': tmpHand[0], 'bid': int(tmpHand[1])}
    newHand['type'] = determineHandType1(newHand['hand'])
    return newHand


def makeHandDictType2(handStr):
    tmpHand = copy.deepcopy(handStr)
    tmpHand = tmpHand.split(' ')
    tmpHand[0] = ' '.join(tmpHand[0])
    tmpHand[0] = tmpHand[0].replace('T', '10')
    tmpHand[0] = tmpHand[0].replace('J', '1')
    tmpHand[0] = tmpHand[0].replace('Q', '12')
    tmpHand[0] = tmpHand[0].replace('K', '13')
    tmpHand[0] = tmpHand[0].replace('A', '14')
    tmpHand[0] = tmpHand[0].split(' ')
    tmpHand[0] = [int(num_str) for num_str in tmpHand[0]]

    newHand = {'hand': tmpHand[0], 'bid': int(tmpHand[1])}
    newHand['type'] = determineHandType2(newHand['hand'])
    return newHand


# --- Start here ---
scriptDir = os.path.dirname(__file__)
relFilePath = 'input.txt'
absFilePath = os.path.join(scriptDir, relFilePath)

with open(absFilePath) as inputFile:
    inputStr = inputFile.read()

inputList = inputStr.splitlines()

# Parse input
handListType1 = []
handListType2 = []
for line in inputList:
    handType1 = makeHandDictType1(line)
    handListType1.append(handType1)
    handType2 = makeHandDictType2(line)
    handListType2.append(handType2)


# Part1
sortedHandListType1 = []
for type in HandType.__members__.values():
    typeDrawList = [hand for hand in handListType1 if hand.get('type') == type]
    selectionSort(typeDrawList)
    sortedHandListType1 = sortedHandListType1 + typeDrawList

totalWinningsType1 = 0
for i, hand in enumerate(sortedHandListType1):
    sortedHandListType1[i]['rank'] = i + 1
    totalWinningsType1 += sortedHandListType1[i]['rank'] * sortedHandListType1[i]['bid']

print('Part 1: ' + str(totalWinningsType1))

# Part2
sortedHandListType2 = []
for type in HandType.__members__.values():
    typeDrawList = [hand for hand in handListType2 if hand.get('type') == type]
    selectionSort(typeDrawList)
    sortedHandListType2 = sortedHandListType2 + typeDrawList

totalWinningsType2 = 0
for i, hand in enumerate(sortedHandListType2):
    sortedHandListType2[i]['rank'] = i + 1
    totalWinningsType2 += sortedHandListType2[i]['rank'] * sortedHandListType2[i]['bid']

print('Part 2: ' + str(totalWinningsType2))
