inputFile = "day8/day8_1_input.txt"

# https://adventofcode.com/2021/day/8


if __name__ == '__main__':
    print("Seven Segment Search")

    with open(inputFile, "r") as f:
        digitEntries = [tuple(entrie.split(" | ")) for entrie in f.read().strip().split("\n")]

    oneSegments = 2
    fourSegments = 4
    seventSegments = 3
    eightSegments = 7

    nbOfUniqSegments = 0
    for line in digitEntries:
        for digit in line[1].split():
            digitLength = len(digit)
            if eightSegments == digitLength or seventSegments == digitLength or fourSegments == digitLength or oneSegments == digitLength:
                nbOfUniqSegments += 1

    print("part1. Uniq segments for numbers 1,2,7,8: ", nbOfUniqSegments)
