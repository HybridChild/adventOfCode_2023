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


def convertByMap(inputValue, convMap):
    for convRange in convMap:
        if convRange['source start'] <= inputValue < (convRange['source start'] + convRange['length']):
            return convRange['destination start'] + (inputValue - convRange['source start'])
    return inputValue


# --- Start here ---
scriptDir = os.path.dirname(__file__)
relFilePath = 'input.txt'
absFilePath = os.path.join(scriptDir, relFilePath)

with open(absFilePath) as inputFile:
    inputStr = inputFile.read()

almanacStrList = inputStr.splitlines()

# Parse input
almanac = {'seeds': [],
           'seed-to-soil map': [],
           'soil-to-fertilizer map': [],
           'fertilizer-to-water map': [],
           'water-to-light map': [],
           'light-to-temperature map': [],
           'temperature-to-humidity map': [],
           'humidity-to-location map': []}

lastMapTitle = ''
for line in almanacStrList:
    if line.startswith('seeds: '):
        almanac['seeds'] = find_numbers(line)
    elif ':' in line:
        lastMapTitle = line[:-1]
    elif line != '':
        newRange = find_numbers(line)
        almanac[lastMapTitle].append({'destination start': newRange[0], 'source start': newRange[1], 'length': newRange[2]})

# Part 1
seedPropertyList = []
locationList = []
for seedNumber in almanac['seeds']:
    seedProperty                = {'seedNumber': seedNumber}
    seedProperty['soil']        = convertByMap(seedProperty['seedNumber'], almanac['seed-to-soil map'])
    seedProperty['fertilizer']  = convertByMap(seedProperty['soil'], almanac['soil-to-fertilizer map'])
    seedProperty['water']       = convertByMap(seedProperty['fertilizer'], almanac['fertilizer-to-water map'])
    seedProperty['light']       = convertByMap(seedProperty['water'], almanac['water-to-light map'])
    seedProperty['temperature'] = convertByMap(seedProperty['light'], almanac['light-to-temperature map'])
    seedProperty['humidity']    = convertByMap(seedProperty['temperature'], almanac['temperature-to-humidity map'])
    seedProperty['location']    = convertByMap(seedProperty['humidity'], almanac['humidity-to-location map'])
    seedPropertyList.append(seedProperty)
    locationList.append(seedProperty['location'])

print('Part 1: ' + str(min(locationList)))
