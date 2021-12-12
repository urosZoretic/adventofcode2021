inputFile = "day11/day11_1_input.txt"


# https://adventofcode.com/2021/day/11

# for debugging purposes only
def printCurrentArray(octopusArray):
    # print array
    for line in octopusArray:
        print(line)


def findAdjacentOctopuses(octopusArray, y, x):
    adjacent = []
    top = y > 0
    right = x < len(octopusArray[0]) - 1
    bottom = y < len(octopusArray) - 1
    left = x > 0

    if top:
        adjacent.append((y - 1, x))
    if top and right:
        adjacent.append((y - 1, x + 1))
    if right:
        adjacent.append((y, x + 1))
    if bottom and right:
        adjacent.append((y + 1, x + 1))
    if bottom:
        adjacent.append((y + 1, x))
    if bottom and left:
        adjacent.append((y + 1, x - 1))
    if left:
        adjacent.append((y, x - 1))
    if top and left:
        adjacent.append((y - 1, x - 1))

    return adjacent


def flashOctopus(octopusArray, coordinate):
    newFlashingOctopus = []
    adjacent = findAdjacentOctopuses(octopusArray, coordinate[0], coordinate[1])

    for adjacentOctopus in adjacent:
        if octopusArray[adjacentOctopus[0]][adjacentOctopus[1]] == 9:
            newFlashingOctopus.append(adjacentOctopus)

        octopusArray[adjacentOctopus[0]][adjacentOctopus[1]] += 1

    return newFlashingOctopus


def flashOctopusesRecursive(octopusArray, flashArray):
    newFlashingOctopuses = []
    for coordinate in flashArray:
        newFlashingOctopuses += flashOctopus(octopusArray, coordinate)

    if len(newFlashingOctopuses) == 0:
        return
    flashOctopusesRecursive(octopusArray, newFlashingOctopuses)



if __name__ == '__main__':
    print("Dumbo Octopus")
    nbPartsSolver = 0

    with open(inputFile, "r") as f:
        octopusArray = [[int(y) for y in list(entry)] for entry in f.read().strip().split("\n")]
    nbOctopuses = len(octopusArray) * len(octopusArray[0])

    nbSteps = 0
    # printCurrentArray(octopusArray)

    flashCounter = 0
    while True:
        nbOneStepFlashes = 0
        flashingOctopusArray = []
        for y in range(0, len(octopusArray)):
            for x in range(0, len(octopusArray[y])):
                octopusArray[y][x] += 1
                if octopusArray[y][x] > 9:
                    flashingOctopusArray.append((y, x))

        flashOctopusesRecursive(octopusArray, flashingOctopusArray)

        for y in range(0, len(octopusArray)):
            for x in range(0, len(octopusArray[y])):
                if octopusArray[y][x] > 9:
                    octopusArray[y][x] = 0
                    nbOneStepFlashes += 1

        flashCounter += nbOneStepFlashes
        nbSteps += 1
        # print("Step: ", nbSteps)
        # printCurrentArray(octopusArray)
        # print("Flashing octupus: ", flashingOctopusArray)
        """if nbSteps == 2:
            newFlashing = flashOctopus(octopusArray, flashingOctopusArray[0])
            print("Adjecent flash: ", newFlashing)
            printCurrentArray(octopusArray)
            print(flashingOctopusArray + newFlashing)"""

        if nbSteps == 100:  # there should be 100 steps for part1
            print("part1. Octopus flash counter after 100 steps: ", flashCounter)
            nbPartsSolver += 1
            if nbPartsSolver == 2:
                break

        if  nbOneStepFlashes == nbOctopuses:
            print("part2. Firt step when all octupuses flash: ", nbSteps)
            nbPartsSolver += 1
            if nbPartsSolver == 2:
                break
