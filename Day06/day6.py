import os
import re
import math

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
timeList = find_numbers(inputList[0])
distList = find_numbers(inputList[1])
gameList = []
for i in range(len(timeList)):
    gameList.append({'max time': timeList[i], 'current record': distList[i]})

# Part 1
# Distance = speed * time
# speed = time of start
# time = max time - time of start
margin_mult = 1
for i, game in enumerate(gameList):
    best_start_time = math.ceil(game['max time'] / 2)
    iter_start_time = best_start_time
    done = False
    while not done:
        dist = iter_start_time * (game['max time'] - iter_start_time)
        if dist <= game['current record']:
            done = True
            margin = (iter_start_time - best_start_time) * 2
            if game['max time'] % 2 == 0:
                margin -= 1
            gameList[i]['margin'] = margin
        iter_start_time += 1
    margin_mult *= margin

print('Part 1: ' + str(margin_mult))
