import os


def findConnectingPipe(map, here, cameFrom):
    # look north
    if here['symbol'] in 'J|LS':
        if here['position'][0] > 0:
            north = [here['position'][0]-1, here['position'][1]]
            if cameFrom['position'] != north:
                if map[north[0]][north[1]] in '7|FS':
                    return {'position': north, 'symbol': map[north[0]][north[1]], 'direction': 'north'}
    # look south
    if here['symbol'] in '7|FS':
        if here['position'][0] < len(map) - 1:
            south = [here['position'][0]+1, here['position'][1]]
            if cameFrom['position'] != south:
                if map[south[0]][south[1]] in 'J|LS':
                    return {'position': south, 'symbol': map[south[0]][south[1]], 'direction': 'south'}
    # look west
    if here['symbol'] in '7-JS':
        if here['position'][1] > 0:
            west = [here['position'][0], here['position'][1]-1]
            if cameFrom['position'] != west:
                if map[west[0]][west[1]] in 'L-FS':
                    return {'position': west, 'symbol': map[west[0]][west[1]], 'direction': 'west'}
    # look east
    if here['symbol'] in 'F-LS':
        if here['position'][1] < len(map[here['position'][0]]) - 1:
            east = [here['position'][0], here['position'][1]+1]
            if cameFrom['position'] != east:
                if map[east[0]][east[1]] in '7-JS':
                    return {'position': east, 'symbol': map[east[0]][east[1]], 'direction': 'east'}
    return None


def determineMarkSymbol(currentStep, nextStep, adjacentUntouched):
    if currentStep['direction'] == 'north' and adjacentUntouched['located'] == 'west':
        return 'Y'
    if currentStep['direction'] == 'north' and adjacentUntouched['located'] == 'east':
        return 'X'
    if currentStep['direction'] == 'north' and adjacentUntouched['located'] == 'north':
        if nextStep['direction'] == 'east':
            return 'Y'
        if nextStep['direction'] == 'west':
            return 'X'
    
    if currentStep['direction'] == 'south' and adjacentUntouched['located'] == 'west':
        return 'X'
    if currentStep['direction'] == 'south' and adjacentUntouched['located'] == 'east':
        return 'Y'
    if currentStep['direction'] == 'south' and adjacentUntouched['located'] == 'south':
        if nextStep['direction'] == 'east':
            return 'X'
        if nextStep['direction'] == 'west':
            return 'Y'
    
    if currentStep['direction'] == 'east' and adjacentUntouched['located'] == 'north':
        return 'Y'
    if currentStep['direction'] == 'east' and adjacentUntouched['located'] == 'south':
        return 'X'
    if currentStep['direction'] == 'east' and adjacentUntouched['located'] == 'east':
        if nextStep['direction'] == 'north':
            return 'X'
        if nextStep['direction'] == 'south':
            return 'Y'
    
    if currentStep['direction'] == 'west' and adjacentUntouched['located'] == 'north':
        return 'X'
    if currentStep['direction'] == 'west' and adjacentUntouched['located'] == 'south':
        return 'Y'
    if currentStep['direction'] == 'west' and adjacentUntouched['located'] == 'west':
        if nextStep['direction'] == 'north':
            return 'Y'
        if nextStep['direction'] == 'south':
            return 'X'
    return None


def findAdjacentUntouched(map, point):
    adjList = []
    # look north
    if point['position'][0] > 0:
        north = [point['position'][0]-1, point['position'][1]]
        if map[north[0]][north[1]] not in 'SXY':
            adjList.append({'position': north, 'located': 'north'})
    # look south
    if point['position'][0] < len(map) - 1:
        south = [point['position'][0]+1, point['position'][1]]
        if map[south[0]][south[1]] not in 'SXY':
            adjList.append({'position': south, 'located': 'south'})
    # look west
    if point['position'][1] > 0:
        west = [point['position'][0], point['position'][1]-1]
        if map[west[0]][west[1]] not in 'SXY':
            adjList.append({'position': west, 'located': 'west'})
    # look east
    if point['position'][1] < len(map[point['position'][0]]) - 1:
        east = [point['position'][0], point['position'][1]+1]
        if map[east[0]][east[1]] not in 'SXY':
            adjList.append({'position': east, 'located': 'east'})
    return adjList


def flood_fill(map, pos, markSymbol, outsideSymbol, symbolCounter):
    if markSymbol == outsideSymbol[0]:
        return  # to avoid exceeding maximum recursion depth
    if pos[0] < 0 or pos[0] >= len(map) or pos[1] < 0 or pos[1] >= len(map[0]):
        outsideSymbol[0] = markSymbol
        return
    if map[pos[0]][pos[1]] in 'SXY':
        return
    
    map[pos[0]][pos[1]] = markSymbol
    symbolCounter[markSymbol] += 1

    # Explore neighboring coordinates
    flood_fill(map, [pos[0] + 1, pos[1]], markSymbol, outsideSymbol, symbolCounter)
    flood_fill(map, [pos[0] - 1, pos[1]], markSymbol, outsideSymbol, symbolCounter)
    flood_fill(map, [pos[0], pos[1] + 1], markSymbol, outsideSymbol, symbolCounter)
    flood_fill(map, [pos[0], pos[1] - 1], markSymbol, outsideSymbol, symbolCounter)


# --- Start here ---
scriptDir = os.path.dirname(__file__)
relFilePath = 'input.txt'
absFilePath = os.path.join(scriptDir, relFilePath)

with open(absFilePath) as inputFile:
    inputStr = inputFile.read()

mapSketch = inputStr.splitlines()

# Find starting coordinate and convert strings to lists
for row, line in enumerate(mapSketch):
    col = line.find('S')
    if col != -1:
        startPos = {'position': [row, col], 'symbol': 'S'}
    mapSketch[row] = list(line)

# Part 1: trace loop and find farthest point
loopRoute = []
currentPos = startPos
previousPos = startPos
done = False
while not done:
    nextPos = findConnectingPipe(mapSketch, currentPos, previousPos)
    if nextPos['symbol'] == startPos['symbol']:
        done = True
    loopRoute.append(nextPos)
    mapSketch[nextPos['position'][0]][nextPos['position'][1]] = 'S' # mark loop tiles
    previousPos = currentPos
    currentPos = nextPos

# calculate distance to farthest point
farthestDist = int(len(loopRoute) / 2)
print('Part 1: ' + str(farthestDist))

# Part 2: find encapsulated area
outsideSymbol = ['']
symbolCounter = {'X': 0, 'Y': 0}
for i, currentStep in enumerate(loopRoute):
    adjacentUntouchedList = findAdjacentUntouched(mapSketch, currentStep)
    for adjacentUntouched in adjacentUntouchedList:
        nextStep = loopRoute[i+1] if i < len(loopRoute)-1 else loopRoute[0]
        markSymbol = determineMarkSymbol(currentStep, nextStep, adjacentUntouched)
        flood_fill(mapSketch, adjacentUntouched['position'], markSymbol, outsideSymbol, symbolCounter)

insideSymbol = 'X' if outsideSymbol[0] == 'Y' else 'Y'
print('Part 2: ' + str(symbolCounter[insideSymbol]))
