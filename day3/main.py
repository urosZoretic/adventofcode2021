inputFile = "./day3/day3_1_input.txt"


# https://adventofcode.com/2021/day/3

def getColumnMaxBits(rowIndex, lines):
    sumOnes = 0
    sumZeros = 0
    for row in lines:
        match row[rowIndex]:
            case 0:
                sumZeros += 1
            case 1:
                sumOnes += 1
    if sumZeros > sumOnes:
        return "0"
    elif sumOnes > sumZeros:
        return "1"
    else:
        print("Equality:: use 1 for index: ", rowIndex)
        return "1"


if __name__ == '__main__':
    print("Binary diagnostic")

    with open(inputFile, "r") as f:
        lines = [[int(y) for y in list(x)] for x in f.read().strip().split('\n')]

    rowLen = len(lines[0])
    gamaRate = ''
    epsilonRate = ''
    for i in range(0, rowLen):
        gamaRate += getColumnMaxBits(i, lines)

    # epsilon rate is basically inverted gamaRate
    epsilonRate = gamaRate.replace('1', '2').replace('0', '1').replace('2', '0')
    print("part1. gama * epsilon rate in decimal: ", int(gamaRate, 2) * int(epsilonRate, 2))

    oxigenGenerator = lines
    co2scrubberRating = lines

    # find oxigen generator
    rowIndex = 0
    while len(oxigenGenerator) != 1 or rowIndex > rowLen:
        mostCommonColumnBit02 = int(getColumnMaxBits(rowIndex, oxigenGenerator))
        # keep rows which match mostCommonColumnBit02
        oxigenGenerator = [v for v in oxigenGenerator if v[rowIndex] == mostCommonColumnBit02]
        rowIndex += 1


    # find co2 scrubber rating
    rowIndex = 0
    while len(co2scrubberRating) != 1 or rowIndex > rowLen:
        mostCommonColumnBitCO2 = int(getColumnMaxBits(rowIndex, co2scrubberRating))
        # keep rows which not match mostCommonColumnBitCO2
        co2scrubberRating = [v for v in co2scrubberRating if v[rowIndex] != mostCommonColumnBitCO2]
        rowIndex += 1

    if len(co2scrubberRating) == 1 and len(oxigenGenerator) == 1:
        print("part2. oxigenGenerator * co2Scrubber: ",
              int(''.join(map(str, oxigenGenerator[0])), 2) * int(''.join(map(str, co2scrubberRating[0])), 2))
    else:
        print("part2.. something went wrong")
