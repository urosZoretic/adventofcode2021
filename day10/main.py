inputFile = "day10/day10_1_input.txt"

# https://adventofcode.com/2021/day/10

def stackMatching(stack, matchChar):
    if stack[-1] != matchChar:
        # print("WRONG line ending: ", navigationChar)
        return False
    stack.pop()
    return True

if __name__ == '__main__':
    print("Syntax Scoring")

    with open(inputFile, "r") as f:
        navigationSubsystem = [entry for entry in f.read().strip().split("\n")]

    # print(navigationSubsystem)
    invalidCharScores = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
    }
    validCharScores = {
        "(": 1,  # complete )
        "[": 2,  # complete ]
        "{": 3,  # complete }
        "<": 4   # complete >
    }
    completionStringScoresLIst = []

    systaxErrorScore = 0

    for subsystem in navigationSubsystem:
        # FIFO -- first in first out
        stack = []
        isOk = True
        for navigationChar in subsystem:
            match navigationChar:
                case "(" | "[" | "{" | "<":
                    stack.append(navigationChar)
                case ")":
                    # print(stack[-1], navigationChar)
                    if not stackMatching(stack, "("):
                        systaxErrorScore += invalidCharScores[navigationChar]
                        isOk = False
                        break
                case "]":
                    # print(stack[-1], navigationChar)
                    if not stackMatching(stack, "["):
                        systaxErrorScore += invalidCharScores[navigationChar]
                        isOk = False
                        break
                case "}":
                    # print(stack[-1], navigationChar)
                    if not stackMatching(stack, "{"):
                        systaxErrorScore += invalidCharScores[navigationChar]
                        isOk = False
                        break
                case ">":
                    # print(stack[-1], navigationChar)
                    if not stackMatching(stack, "<"):
                        systaxErrorScore += invalidCharScores[navigationChar]
                        isOk = False
                        break
            # print(stack)
        if isOk:
            completionScore = 0
            # print("Incomplete line: ", subsystem, stack)
            for completeChar in stack[::-1]:
                # print(completeChar, end="")
                completionScore = (completionScore * 5) + validCharScores[completeChar]
            # print()
            # print("Score: ", completionScore)
            completionStringScoresLIst.append(completionScore)

    print("part1. Syntax error score: ", systaxErrorScore)
    completionStringScoresLIst.sort()
    print("part2. Middle completion score: ", completionStringScoresLIst[(len(completionStringScoresLIst) - 1) // 2])
