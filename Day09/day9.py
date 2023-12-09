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

inputList = inputStr.splitlines()

# Parse input
OASIS_report = []
for line in inputList:
    OASIS_report.append(find_numbers(line))


