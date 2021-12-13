inputFile = "day13/day13_1_input.txt"


# https://adventofcode.com/2021/day/13

def deleteAndAddKeys(paperDict, keysToPop, keysToAdd):
    for key in keysToPop:
        del paperDict[key]

    for key in keysToAdd:
        if key not in paperDict:
            paperDict[key] = True


def foldYUp(paperDict, y):
    keysToPop = []
    keysToAdd = []

    for key in paperDict:
        if key[0] == y:  # on index zero we have y position
            keysToPop.append(key)
        if key[0] > y:  # we should fold up
            yFoldDiff = key[0] - y
            newYCoordinate = y - yFoldDiff
            keysToAdd.append((newYCoordinate, key[1]))
            keysToPop.append(key)

    deleteAndAddKeys(paperDict, keysToPop, keysToAdd)


def foldXLeft(paperDict, x):
    keysToPop = []
    keysToAdd = []

    for key in paperDict:
        if key[1] == x:  # on index one we have x position
            keysToPop.append(key)
        if key[1] > x:  # we should fold left
            xFoldDiff = key[1] - x
            newXCoordinate = x - xFoldDiff
            keysToAdd.append((key[0], newXCoordinate))
            keysToPop.append(key)

    deleteAndAddKeys(paperDict, keysToPop, keysToAdd)


if __name__ == '__main__':
    with open(inputFile, "r") as f:
        input = f.read().split("\n")

    # print(input)
    transparentPaperDict = {}
    folds = []
    isFolds = False

    for line in input:
        if line == '':
            isFolds = True
            continue
        if isFolds:
            folds.append(line)
        else:
            x, y = line.split(",")
            transparentPaperDict[(int(y), int(x))] = True

    nbFolds = 0
    for fold in folds:
        command, value = fold.split("=")
        # print(command, int(value))
        if command == "fold along y":
            foldYUp(transparentPaperDict, int(value))
        if command == "fold along x":
            foldXLeft(transparentPaperDict, int(value))

        nbFolds += 1
        if nbFolds == 1:
            print("part1. Visible dots after first fold: ", len(transparentPaperDict))

    maxX = 0
    maxY = 0
    for key in transparentPaperDict:
        if key[0] > maxY:
            maxY = key[0]
        if key[1] > maxX:
            maxX = key[1]
    resultPrint = []
    for i in range(0, maxY + 1):
        resultPrint.append(["."] * (maxX + 1))

    for key in transparentPaperDict:
        resultPrint[key[0]][key[1]] = "#"

    # print result in console
    print("part2. ASCI ART :)")
    for line in resultPrint:
        for value in line:
            print(value, end="")
        print()
