import os
import queue as PQ
import time


def findPotentialPaths(map, current):
    potentialPaths = []
    # look up
    if      current['position'][0] > 0 \
        and current['history'][0][0] < current['position'][0] + 3:
        potentialPaths.append([current['position'][0] - 1, current['position'][1]])
    # look down
    if      current['position'][0] < len(map) - 1 \
        and current['history'][0][0] > current['position'][0] - 3:
        potentialPaths.append([current['position'][0] + 1, current['position'][1]])
    # look left
    if      current['position'][1] > 0 \
        and current['history'][0][1] < current['position'][1] + 3:
        potentialPaths.append([current['position'][0], current['position'][1] - 1])
    # look right
    if      current['position'][1] < len(map[current['position'][0]]) - 1 \
        and current['history'][0][1] > current['position'][1] - 3:
        potentialPaths.append([current['position'][0], current['position'][1] + 1])
    
    return potentialPaths


def traceRoute(heatLossMap, routePriQue, visitedDict, goalPos):
    current = routePriQue.get()
    currentHeatLoss = current[0]
    current = current[1][1]
    potentialPaths = findPotentialPaths(heatLossMap, current)

    for pathPos in potentialPaths:
        if str(pathPos) not in visitedDict.keys():
            heatLoss = heatLossMap[pathPos[0]][pathPos[1]] + currentHeatLoss
            history = current['history'][1:3]
            history.extend([current['position']])
            routePriQue.put([heatLoss, [[goalPos[0]-pathPos[0], goalPos[1]-pathPos[1]], {'position': pathPos, 'history': history}]])
            visitedDict[str(pathPos)] = heatLoss
    
    return current

# 2>>34^>>>1323
# 32v>>>35v5623
# 32552456v>>54
# 3446585845v52
# 4546657867v>6
# 14385987984v4
# 44578769877v6
# 36378779796v>
# 465496798688v
# 456467998645v
# 12246868655<v
# 25465488877v5
# 43226746555v>

# --- Start here ---
start_time = time.time()

scriptDir = os.path.dirname(__file__)
relFilePath = 'example.txt'
absFilePath = os.path.join(scriptDir, relFilePath)

with open(absFilePath) as inputFile:
    heatLossMap = [list(row) for row in inputFile.read().splitlines()]

for row in range(len(heatLossMap)):
    for col in range(len(heatLossMap[row])):
        heatLossMap[row][col] = int(heatLossMap[row][col])

# Part 1
startHeatLoss = 0
startPosition = (0, 0)
goalPosition = (len(heatLossMap)-1, len(heatLossMap[0])-1)

current = {'position': list(startPosition), 'history': [list(startPosition), list(startPosition), list(startPosition)]}
visitedDict = {str(current['position']): startHeatLoss}
routePriQue = PQ.PriorityQueue()
routePriQue.put([startHeatLoss, [startHeatLoss, current]])

while current['position'] != list(goalPosition):
    current = traceRoute(heatLossMap, routePriQue, visitedDict, goalPosition)

print('Part 1: ' + str(visitedDict[str(current['position'])]))

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")
