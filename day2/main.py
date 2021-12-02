inputFile = "./day2/day2_1_input.txt"
# https://adventofcode.com/2021/day/1
if __name__ == '__main__':
    print("DIVE: how to pilot")

    # sliding window size of 3
    with open(inputFile, "r") as f:
        lines = f.read().strip().split('\n')

    horPosition = 0  # the same for part1 and part2 of the puzzle
    depth = 0

    depthPart2 = 0
    aim = 0

    for line in lines:
        instructions = line.strip().split(" ") # index0: type, index1: value
        match instructions[0]:
            case "forward":
                horPosition += int(instructions[1])
                depthPart2 += aim * int(instructions[1])
            case "down":
                depth += int(instructions[1])
                aim += int(instructions[1])
            case "up":
                depth -= int(instructions[1])
                aim -= int(instructions[1])

    print("part1. Final horPosition * depth: ", horPosition * depth)
    print("part2. Final horPosition * depth: ", horPosition * depthPart2)
