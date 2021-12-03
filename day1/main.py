inputFile = "day1/day1_1_input.txt"
# https://adventofcode.com/2021/day/1
if __name__ == '__main__':
    print("SONAR SWEEP")
    nbIncreased = 0
    with open(inputFile, "r") as f:
        prevValue = 0

        for index, value in enumerate(f):
            value = int(value)
            if index != 0 and prevValue < value:
                nbIncreased += 1
            prevValue = value
    print("part1: ", nbIncreased)

    # sliding window size of 3
    with open(inputFile, "r") as f:
        lines = [int(value) for value in f.read().strip().split('\n')]

    nbIncreased = 0
    currentSum = sum(lines[:3])
    prevSum = currentSum
    index = 1
    for value in lines[1:-2]:
        currentSum -= lines[index - 1]
        currentSum += lines[index + 2]

        if currentSum > prevSum:
            nbIncreased += 1
        prevSum = currentSum
        index += 1

    print("part2: ", nbIncreased)
