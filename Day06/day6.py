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
raceList = []
for i in range(len(timeList)):
    raceList.append({'max time': timeList[i], 'current record': distList[i]})

# Part 1
# Distance = speed * time
# speed = time of start
# time = max time - time of start

actual_max_time_str = ''
actual_record_str = ''
margin_mult = 1
for i, race in enumerate(raceList):
    best_start_time = math.ceil(race['max time'] / 2)
    iter_start_time = best_start_time
    done = False
    while not done:
        dist = iter_start_time * (race['max time'] - iter_start_time)
        if dist <= race['current record']:
            done = True
            margin = (iter_start_time - best_start_time) * 2
            if race['max time'] % 2 == 0:
                margin -= 1
            raceList[i]['margin'] = margin
        iter_start_time += 1
    margin_mult *= margin

    # find actual race time and record for part 2
    actual_max_time_str += str(race['max time'])
    actual_record_str += str(race['current record'])

print('Part 1: ' + str(margin_mult))


# Part 2 - run again with actual race max time and record
actual_max_time = int(actual_max_time_str)
actual_record = int(actual_record_str)

best_start_time = math.ceil(actual_max_time / 2)
iter_start_time = best_start_time
actual_margin = 0
done = False
while not done:
    dist = iter_start_time * (actual_max_time - iter_start_time)
    if dist <= actual_record:
        done = True
        actual_margin = (iter_start_time - best_start_time) * 2
        if actual_max_time % 2 == 0:
            actual_margin -= 1
    iter_start_time += 1

print('Part 2: ' + str(actual_margin))
