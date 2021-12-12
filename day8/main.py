inputFile = "day8/day8_1_input.txt"

# https://adventofcode.com/2021/day/8

## part2 solution has been inspired by other people...


if __name__ == '__main__':
    print("Seven Segment Search")

    part1 = part2 = 0

    with open(inputFile, "r") as f:
        digitEntries = [tuple(entrie.split(" | ")) for entrie in f.read().strip().split("\n")]

    for line in digitEntries:
        # print(line)
        d = {
            l: set(s) for s in line[0].split() if (l := len(s)) in (2, 4)
        }
        # print(d)
        n = ""
        for digit in line[1].split():
            digitLength = len(digit)
            if digitLength == 2:
                n += "1"; part1 += 1
            elif digitLength == 4:
                n += "4"; part1 += 1
            elif digitLength == 3:
                n += "7"; part1 += 1
            elif digitLength == 7:
                n += "8"; part1 += 1
            elif digitLength == 5:
                s = set(digit)
                # print("Len five: ", s, s & d[2], s & d[4]) --> get match
                if len(s & d[2]) == 2:
                    n += "3"
                elif len(s & d[4]) == 2:
                    n += "2"
                else:
                    n += "5"
                # print(n)
            else:  # digitLength == 6
                s = set(digit)
                if len(s & d[2]) == 1:
                    n += "6"
                elif len(s & d[4]) == 4:
                    n += "9"
                else:
                    n += "0"
        part2 += int(n)


    print("part1. Uniq segments for numbers 1,2,7,8: ", part1)
    print("part2. decoded digit sum: ", part2)


