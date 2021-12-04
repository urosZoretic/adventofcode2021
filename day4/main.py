inputFile = "./day4/day4_1_input.txt"


# https://adventofcode.com/2021/day/4

class Board:
    boardArray = []

    def __init__(self):
        self.boardArray = []

    def addInputLineToBoard(self, line_data):
        self.boardArray.append([self.__Value(int(num)) for num in line_data.split()])

    def checkAndMarkNumber(self, num):
        for boardLine in self.boardArray:
            for value in boardLine:
                value.markNumber() if value.num == num else None

    def checkForBingo(self):
        # check rows
        for row in self.boardArray:
            nbMarked = 0
            for value in row:
                if value.isMarked: nbMarked += 1
            if nbMarked == len(row):
                return True
        # check columns
        for i in range(len(self.boardArray[0])):
            nbMarked = 0
            for row in self.boardArray:
                if row[i].isMarked: nbMarked += 1
            if nbMarked == len(self.boardArray):
                return True
        return False

    def sumUnmarkedValues(self):
        sum = 0
        for row in self.boardArray:
            for value in row:
                if not value.isMarked: sum += value.num
        return sum

    # utility for debugging only
    def printBoard(self):
        for boardLine in self.boardArray:
            for value in boardLine:
                print("(", value.isMarked, value.num, "), ", end="")

            print()

    class __Value:
        num = 0
        isMarked = False

        def __init__(self, num):
            self.num = num

        def markNumber(self):
            self.isMarked = True


def solveBingoPart1FirstToWin(randNumbers, boards):
    for randNum in randNumbers:
        for board in boards:
            board.checkAndMarkNumber(randNum)
            isBingo = board.checkForBingo()
            if isBingo:
                # board.printBoard()
                return randNum * board.sumUnmarkedValues()


def solveBingoPart2LastToWin(randNumbers, boards):
    for indexNumber, randNum in enumerate(randNumbers):
        losingIndexes = []
        for boardIndexLosing, _ in enumerate(boards):
            boards[boardIndexLosing].checkAndMarkNumber(randNum)
            isBingo = boards[boardIndexLosing].checkForBingo()
            if isBingo:
                losingIndexes.append(boardIndexLosing)
        boards = [boards[index] for index, _ in enumerate(boards) if index not in losingIndexes]
        if len(boards) == 1:
            # Then solve problem part1 but from current number index and with one board in the array.
            # to check one the last board wins
            return solveBingoPart1FirstToWin(randNumbers[indexNumber + 1:], boards)


if __name__ == '__main__':
    print("Giant squid")

    randNumbers = []
    boards = []
    boardIndex = -1

    with open(inputFile, "r") as f:
        for line in f:
            if len(randNumbers) == 0:
                randNumbers = [int(num) for num in line.strip().split(",")]
            else:
                if len(line.strip()) == 0:
                    boardIndex += 1
                    boards.append(Board())
                else:
                    boards[boardIndex].addInputLineToBoard(line)

    # print("Rand numbers for bingo: ", randNumbers)
    # boards[0].printBoard()

    print("part1. Bingo score winning board: ", solveBingoPart1FirstToWin(randNumbers, boards))
    print("part2. Bingo score losing board: ", solveBingoPart2LastToWin(randNumbers, boards))
