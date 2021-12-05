inputFile = "day5/day5_1_input.txt"


# https://adventofcode.com/2021/day/5

def coordinate(obj):
    return tuple(map(int, obj.split(',')))


def draw_horizontal_line(grid, y, x, x1):
    for i in range(min(x, x1), max(x, x1) + 1): # inclusive.. at least one point will be added if cooardinates are all the same
        if (i, y) not in grid:
            grid[(i, y)] = 1
        else:
            grid[(i, y)] += 1


def draw_vertical_line(grid, x, y, y1):
    for i in range(min(y, y1), max(y, y1) + 1): # inclusive.. at least one point will be added if cooardinates are all the same
        if (x, i) not in grid:
            grid[(x, i)] = 1
        else:
            grid[(x, i)] += 1


def draw_diagonal_line(grid, x, y, x1, y1):
    intersections = 0
    lineLength = abs(x - x1)

    for _ in range(lineLength + 1): # inclusive.. at least one point will be added if cooardinates are all the same
        if (x, y) not in grid:
            grid[(x, y)] = 1
        else:
            grid[(x, y)] += 1

        # go to next diagonal point based on direction (up or down)
        x += 1 if x1 > x else -1
        y += 1 if y1 > y else -1

    return intersections


def getGridNbIntersections(grid):
    nbIntersections = 0
    for value in grid.values():
        if value >= 2:
            nbIntersections += 1
    return nbIntersections

if __name__ == '__main__':
    print("Hydrothermal Venture")

    # grid is passed to the function by reference (pointer internally)
    grid = {}
    grid2 = {}

    with open(inputFile, "r") as f:
        for line in f:
            splitCoordinates = line.strip().split(" -> ")
            p1, p2 = coordinate(splitCoordinates[0]), coordinate(splitCoordinates[1])
            # draw horizontal line if p1[1] and p2[1] are the same (y position is the same)
            if p1[1] == p2[1]:
                draw_horizontal_line(grid, p1[1], p1[0], p2[0])
                draw_horizontal_line(grid2, p1[1], p1[0], p2[0])
            # draw vertical line if p1[0] and p2[0] are the same (x position is the same)
            elif p1[0] == p2[0]:
                draw_vertical_line(grid, p1[0], p1[1], p2[1])
                draw_vertical_line(grid2, p1[0], p1[1], p2[1])
            else:
                draw_diagonal_line(grid2, p1[0], p1[1], p2[0], p2[1])

    # nbIntersection part1
    print("part1. NbIntersections with at least two lines: ", getGridNbIntersections(grid))
    print("part2. NbIntersections with at least two lines. diagonal included: ", getGridNbIntersections(grid2))
