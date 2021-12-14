import sys
from collections import Counter, defaultdict

inputFile = "day14/day14_1_input.txt"


# https://adventofcode.com/2021/day/14


def calculate(polymer, rules, numSteps):
    # print(rules)
    pairCount = defaultdict(int)

    for i in range(len(polymer) - 1):
        currentPair = polymer[i:i + 2]
        pairCount[currentPair] += 1

    # print(pairCount)

    # last letter never changes
    last = polymer[-1]
    for i in range(numSteps):
        newPairCount = defaultdict(int)
        """
        Now loop through the keys in the pairCount dictionary
        For each key, see if it exists in the reaction dictionary
        If it does, add to new Pair Count the appropriate pairs. (e.g. if the pair is AB and appears 10 times, and you have the rule AB -> C in your rules dictionary, add/increment the entries AC=10 and CB=10)
        If it doesn't, just add the pair and its own count to the new Pair Count dictionary (e.g. if the pair is AB and AB does NOT appear in your rules dictionary, just add/increment AB=10 to your new Pair Count dictionary)
        """
        for pair in pairCount:
            # print(pair)
            if pair in rules:
                # newPairs = (pair[0] + rules[pair], rules[pair] + pair[1])
                # print("new pairs: ", newPairs)
                newPairCount[pair[0] + rules[pair]] += pairCount[pair]  ## increment newPair with previousValues
                newPairCount[rules[pair] + pair[1]] += pairCount[pair]  ## increment newPair with previousValues
            else:
                newPairCount[pair] += pairCount[pair]

        pairCount = newPairCount

    # print("Pair count: ",  pairCount)
    charCount = defaultdict(int)
    for pair in pairCount:
        charCount[pair[0]] += pairCount[pair]

    charCount[last] += 1
    # print(charCount)

    maxNumber = 0
    minNumber = sys.maxsize
    for c in charCount:
        maxNumber = max(charCount[c], maxNumber)
        minNumber = min(charCount[c], minNumber)

    return maxNumber - minNumber


if __name__ == '__main__':
    rules = {}

    print("Extended Polymerization")
    with open(inputFile, "r") as f:
        input = f.read().split("\n")

    # print(input)
    polymer = ""
    isRules = False

    for line in input:
        # print(line)
        if line == "":
            isRules = True
            continue

        if not isRules:
            polymer = line
        else:
            key, value = line.split(" -> ")
            rules[key] = value

    origPolymer = polymer
    # print(polymer)
    # print(rules)
    # NOTE: To heavy for part 2
    nbSteps = 0
    while True:
        nbSteps += 1
        newPolymer = ""
        for charIndex in range(0, len(polymer) - 1):
            # print(polymer[charIndex] + polymer[charIndex+1])
            if polymer[charIndex] + polymer[charIndex + 1] in rules:
                newPolymer += polymer[charIndex] + rules[polymer[charIndex] + polymer[charIndex + 1]]
        newPolymer += polymer[-1]
        polymer = newPolymer
        # print("new polymer after: : ", nbSteps)

        if nbSteps == 10:
            mostCommonNB = 0
            leastCommonNb = 0
            counter = Counter(polymer).most_common()
            # print(counter)
            # print(counter[0][1], counter[-1][1])
            print("part1. 10 steps. Quantity of subtraction: most and least common element in polymer: ",
                  counter[0][1] - counter[-1][1])
            break

    print("part2. 40 steps. Quantity of subtraction: most and least common element in polymer: ",
          calculate(origPolymer, rules, 40))
