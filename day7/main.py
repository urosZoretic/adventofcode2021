import sys

inputFile = "day7/day7_1_input.txt"


# https://adventofcode.com/2021/day/7

def returnMin(currentMin, tmpNum):
    if currentMin < tmpNum:
        return currentMin

    return tmpNum


if __name__ == '__main__':
    # NOTE... binary search implementation should be faster... but ok.. "brute force" solution works
    print("The Treachery of Whales")

    with open(inputFile, "r") as f:
        crabPosition = [int(num) for num in f.read().strip().split(",")]

    minFuel = sys.maxsize  # only one sys lib to get max number of int
    minFuelPart2 = sys.maxsize

    for n in range(min(crabPosition), max(crabPosition)):  # possible min positions
        tmpFuel = 0
        tmpFuelPar2 = 0
        for position in crabPosition:
            nbSteps = abs(position - n)
            tmpFuel += nbSteps

            tmpFuelPar2 += sum(range(1, nbSteps + 1))

        minFuel = returnMin(minFuel, tmpFuel)
        minFuelPart2 = returnMin(minFuelPart2, tmpFuelPar2)

    print("part1. Min fuel spent for submarine crab alignment: ", minFuel)
    print("part2. Min fuel spent for submarine crab alignment. One step cost more: ", minFuelPart2)
