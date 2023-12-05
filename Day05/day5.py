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
relFilePath = 'example.txt'
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
        almanac[lastMapTitle].append({'destination range start': newRange[0], 'source range start': newRange[1], 'range length': newRange[2]})

# Part 1