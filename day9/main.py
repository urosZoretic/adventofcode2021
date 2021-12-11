inputFile = "day9/day9_1_input.txt"

# https://adventofcode.com/2021/day/9

def floodfill(matrix, x, y, basinPoints):
    if matrix[y][x] == 9 or (y, x) in basinPoints:
        return basinPoints

    basinPoints.add((y, x))
    if x > 0:
        floodfill(matrix, x-1, y, basinPoints)
    if x < len(matrix[y]) - 1:
        floodfill(matrix, x + 1, y, basinPoints)
    if y > 0:
        floodfill(matrix, x, y-1, basinPoints)
    if y < len(matrix) - 1:
        floodfill(matrix, x, y + 1, basinPoints)

    return basinPoints

if __name__ == '__main__':
    print("Smoke Basin")

    with open(inputFile, "r") as f:
        heightMapArray = [[int(y) for y in list(entry)] for entry in f.read().strip().split("\n")]

    riskLevelLowPoints = 0
    lowpoints = set()
    for y in range(len(heightMapArray)):
        for x in range(len(heightMapArray[y])):
            count = 0
            if x != 0:
                if heightMapArray[y][x] < heightMapArray[y][x - 1]:
                    count += 1
            else:
                count += 1
            if x != len(heightMapArray[y]) - 1:
                if heightMapArray[y][x] < heightMapArray[y][x + 1]:
                    count += 1
            else:
                count += 1
            if y != 0:
                if heightMapArray[y][x] < heightMapArray[y - 1][x]:
                    count += 1
            else:
                count += 1
            if y != len(heightMapArray) - 1:
                if heightMapArray[y][x] < heightMapArray[y + 1][x]:
                    count += 1
            else:
                count += 1
            if count == 4:
                riskLevelLowPoints += heightMapArray[y][x] + 1
                lowpoints.add((y, x))

    print("part1. Risk level lo points: ", riskLevelLowPoints)
    # print(lowpoints, len(lowpoints))

    ## part2 -- finding basin... floodfill
    maxNbBasin = [0, 0, 0]
    for point in lowpoints:
        basinPoints = floodfill(heightMapArray, point[1], point[0], set())
        # print("Basin points: ",  basinPoints, len(basinPoints), point)
        # find min in max basin size
        minIndex = maxNbBasin.index(min(maxNbBasin))
        if maxNbBasin[minIndex] < len(basinPoints):
            maxNbBasin[minIndex] = len(basinPoints)

    # print("Max basin points: ", maxNbBasin)
    maxBasinScore = 1
    for basinSize in maxNbBasin:
        maxBasinScore = maxBasinScore * basinSize

    print("part2. Max basin multiply score: ", maxBasinScore)