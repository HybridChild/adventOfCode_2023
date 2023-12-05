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


def reverseByMap(inputValue, convMap):
    for convRange in convMap:
        if convRange['destination start'] <= inputValue < (convRange['destination start'] + convRange['length']):
            return convRange['source start'] + (inputValue - convRange['destination start'])
    return inputValue


def findSeedProperties(seedNumber, almanac):
    seed                = {'seedNumber': seedNumber}
    seed['soil']        = convertByMap(seed['seedNumber'] , almanac['seed-to-soil map'])
    seed['fertilizer']  = convertByMap(seed['soil']       , almanac['soil-to-fertilizer map'])
    seed['water']       = convertByMap(seed['fertilizer'] , almanac['fertilizer-to-water map'])
    seed['light']       = convertByMap(seed['water']      , almanac['water-to-light map'])
    seed['temperature'] = convertByMap(seed['light']      , almanac['light-to-temperature map'])
    seed['humidity']    = convertByMap(seed['temperature'], almanac['temperature-to-humidity map'])
    seed['location']    = convertByMap(seed['humidity']   , almanac['humidity-to-location map'])
    return seed

def findSeedByLocation(location, almanac):
    seed                = {'location': location}
    seed['humidity']    = reverseByMap(seed['location']   , almanac['humidity-to-location map'])
    seed['temperature'] = reverseByMap(seed['humidity']   , almanac['temperature-to-humidity map'])
    seed['light']       = reverseByMap(seed['temperature'], almanac['light-to-temperature map'])
    seed['water']       = reverseByMap(seed['light']      , almanac['water-to-light map'])
    seed['fertilizer']  = reverseByMap(seed['water']      , almanac['fertilizer-to-water map'])
    seed['soil']        = reverseByMap(seed['fertilizer'] , almanac['soil-to-fertilizer map'])
    seed['seedNumber']  = reverseByMap(seed['soil']       , almanac['seed-to-soil map'])
    return seed


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
locationList = []
for seedNumber in almanac['seeds']:
    seed = findSeedProperties(seedNumber, almanac)
    locationList.append(seed['location'])

print('Part 1: ' + str(min(locationList)))

# Part 2
rangeList = []
i = 0
while i < len(almanac['seeds']):
    seedStart = almanac['seeds'][i]
    seedRange = almanac['seeds'][i+1]
    rangeList.append([seedStart, seedStart + seedRange])
    i += 2

location = -1
done = False
while not done:
    location += 1
    seed = findSeedByLocation(location, almanac)
    for ran in rangeList:
        if ran[0] <= seed['seedNumber'] < ran[1]:
            done = True

print('Part 2: ' + str(location))
