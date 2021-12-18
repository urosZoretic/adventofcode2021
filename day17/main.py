inputFile = "day17/day17_1_input.txt" ## no need to actually read input.. its is to small.. hardoced in code


# https://adventofcode.com/2021/day/17


class Probe:
    # probe always start at position 0, 0
    x = 0
    y = 0
    velocityX = 0
    velocityY = 0

    targetLeft = 0
    targetTop = 0
    targetRight = 0
    targetBottom = 0

    highestY = 0


    def __init__(self, vx, vy, targetLeft, targetTop, targetRight, targetBottom):
        self.velocityX = vx
        self.velocityY = vy

        self.targetLeft = targetLeft
        self.targetTop = targetTop
        self.targetRight = targetRight
        self.targetBottom = targetBottom
    """
    The probe's x position increases by its x velocity.
    The probe's y position increases by its y velocity.
    Due to drag, the probe's x velocity changes by 1 toward the value 0; that is, it decreases by 1 if it is greater than 0, increases by 1 if it is less than 0, or does not change if it is already 0.
    Due to gravity, the probe's y velocity decreases by 1.
    """

    def oneStep(self):
        self.x += self.velocityX
        self.y += self.velocityY

        if self.velocityX > 0:
            self.velocityX -= 1
        elif self.velocityX < 0:
            self.velocityX += 1

        self.velocityY -= 1

        if self.highestY < self.y:
            self.highestY = self.y

    def aboveBottomOfTarget(self):
        return self.y > self.targetBottom

    def insideTarget(self):
        return self.x >= self.targetLeft and self.x <= self.targetRight and self.y >= self.targetBottom and self.y <= self.targetTop

    def printState(self):
        print("State: ")
        print("x: ", self.x, "y: ", self.y)
        print("velocityX: ", self.velocityX, "velocityY: ", self.velocityY)



def calcForOneInitialVelocity(vx, vy):
    # probe = Probe(vx, vy, 20, -5, 30, -10) # test input
    probe = Probe(vx, vy, 241, -49, 275, -75) # real input
    while probe.aboveBottomOfTarget():
        probe.oneStep()
        # probe.printState()
        # print("--------------------")
        if probe.insideTarget():
            return probe.highestY, True

    return 0, False

if __name__ == "__main__":
    print("Trick shot")

    highestY = 0
    countPossibleOptions = 0

    for vx in range(0, 1000):
        print("vx: ", vx)
        for vy in range(-1000, 1000):
            highTmpY, isInTarget = calcForOneInitialVelocity(vx, vy)
            if isInTarget:
                countPossibleOptions += 1
                if highestY < highTmpY:
                    highestY = highTmpY

    print("part1. HighestY to reach target: ", highestY)
    print("part2. all possible options: ", countPossibleOptions)