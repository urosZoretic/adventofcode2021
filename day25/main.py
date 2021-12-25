import copy
print("Sea Cucumber")

def printArray(cucumberArray):
    for line in cucumberArray:
        for value in line:
            print(value, end="")
        print()

def checkIfAlreadyMove(moveDict, y, x):
    return (y, x) in moveDict

def moveCucumbers(cucumberArray, moveType, movesDict, origList):
    # print("ORIGINAL: ", moveType)
    # printArray(origList)
    # print("KONC: ", origList[0][7])
    hasMoved = False
    for y in range(0, len(cucumberArray)):
        for x in range(0, len(cucumberArray[0])):
            if moveType == cucumberArray[y][x]:
                if moveType == ">" and origList[y][(x+1) % len(origList[0])] == "." and not checkIfAlreadyMove(movesDict, y, x):
                    # print("moving: ", movesDict, (y, x), checkIfAlreadyMove(movesDict, y, x))
                    cucumberArray[y][x] = "."
                    cucumberArray[y][(x+1) % len(cucumberArray[0])] = moveType
                    movesDict[(y, (x+1) % len(cucumberArray[0]))] = True
                    hasMoved = True
                elif moveType == "v" and origList[(y+1) % len(origList)][x] == "." and not checkIfAlreadyMove(movesDict, y, x):
                    """if y == len(cucumberArray)-1:
                        print("moving: ", y, x, origList[0][x])"""
                    cucumberArray[y][x] = "."
                    cucumberArray[(y+1) % len(cucumberArray)][x] = moveType
                    movesDict[((y+1) % len(cucumberArray), x)] = True
                    hasMoved = True
            # print("OMG: ", origList[0][7], y, x)
    return hasMoved

with open("day25/day25_1_input.txt", "r") as f:
    cucumberArray = [[y for y in list(entry)] for entry in f.read().strip().split("\n")]

#printArray(cucumberArray)
# print("-------------------------")

nbSteps = 0

while True:
    nbSteps += 1
    print("Step: ", nbSteps)
    hasMovedEast = moveCucumbers(cucumberArray, ">", {}, copy.deepcopy(cucumberArray))
    hasMovedWest = moveCucumbers(cucumberArray, "v", {}, copy.deepcopy(cucumberArray))
    # print("ZARES")
    # printArray(cucumberArray)
    if not hasMovedEast and not hasMovedWest:
        break

print("part1. nbSteps when stop moving: ", nbSteps)