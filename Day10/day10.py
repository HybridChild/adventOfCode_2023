import os
import math


def findConnectingPipe(map, here, cameFrom):
    # look north
    if here['symbol'] in 'J|LS':
        if here['position'][0] > 0:
            north = [here['position'][0]-1, here['position'][1]]
            if cameFrom['position'] != north:
                if map[north[0]][north[1]] in '7|FS':
                    return {'position': north, 'symbol': map[north[0]][north[1]]}
    # look south
    if here['symbol'] in '7|FS':
        if here['position'][0] < len(map) - 1:
            south = [here['position'][0]+1, here['position'][1]]
            if cameFrom['position'] != south:
                if map[south[0]][south[1]] in 'J|LS':
                    return {'position': south, 'symbol': map[south[0]][south[1]]}
    # look west
    if here['symbol'] in '7-JS':
        if here['position'][1] > 0:
            west = [here['position'][0], here['position'][1]-1]
            if cameFrom['position'] != west:
                if map[west[0]][west[1]] in 'L-FS':
                    return {'position': west, 'symbol': map[west[0]][west[1]]}
    # look east
    if here['symbol'] in 'F-LS':
        if here['position'][1] < len(map[here['position'][0]]) - 1:
            east = [here['position'][0], here['position'][1]+1]
            if cameFrom['position'] != east:
                if map[east[0]][east[1]] in '7-JS':
                    return {'position': east, 'symbol': map[east[0]][east[1]]}
    return None



# --- Start here ---
scriptDir = os.path.dirname(__file__)
relFilePath = 'input.txt'
absFilePath = os.path.join(scriptDir, relFilePath)

with open(absFilePath) as inputFile:
    inputStr = inputFile.read()

mapSketch = inputStr.splitlines()

# Find starting coordinate
for row, line in enumerate(mapSketch):
    col = line.find('S')
    if col != -1:
        startPos = {'position': [row, col], 'symbol': 'S'}
        break

# trace loop
loopRoute = [startPos]
currentPos = startPos
previousPos = startPos
done = False
while not done:
    nextPos = findConnectingPipe(mapSketch, currentPos, previousPos)
    if nextPos['symbol'] == startPos['symbol']:
        done = True
    loopRoute.append(nextPos)
    previousPos = currentPos
    currentPos = nextPos

# calculate distance to farthest point
farthestDist = int(math.floor(len(loopRoute) / 2))
print('Part 1: ' + str(farthestDist))
