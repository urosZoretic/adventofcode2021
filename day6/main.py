inputFile = "day6/day6_1_input.txt"

# https://adventofcode.com/2021/day/6

if __name__ == '__main__':
    print("Lanternfish")

    with open(inputFile, "r") as f:
        fishArray = [int(num) for num in f.read().strip().split(",")]
    # for part2... not needed to read array again from file
    origFishArray = fishArray.copy()

    # unsustainable solution for part2... to big array.. memory heavy
    nbDays = 1
    while nbDays <= 80:
        for index in range(0, len(fishArray)):
            if fishArray[index] == 0:
                fishArray[index] = 6
                fishArray.append(8)
                continue

            fishArray[index] -= 1
        nbDays += 1

    print("part1. Nb fish after 80 days: ", len(fishArray))


    ## part 2 --> fish counters
    fishCounter = [0] * 9
    for num in origFishArray:
        fishCounter[num] += 1 # index represent number.. value represent nb fishes for that fish stage

    nbDays = 1
    while nbDays <= 256:
        # each day shift array values to th left.
        nbSpawn = 0
        for i in range(0, len(fishCounter) - 1):
            if i == 0: ## spawn for current day
                nbSpawn = fishCounter[i]
            fishCounter[i] = fishCounter[i + 1]

        # spawn fishes for current day
        fishCounter[8] = nbSpawn # spawn nb fishes
        fishCounter[6] += nbSpawn # reset nbSpawn fished to state 6
        nbDays +=1

    print("part2. After 256 days. Efficient solution: ", sum(fishCounter))