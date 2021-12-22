from collections import defaultdict
import re
from collections import Counter

print("Reactor Reboot")

with open("day22/day22_1_input.txt", "r") as f:
    commands = [entry for entry in f.read().strip().split("\n")]

# print(commands)

cubeDict = defaultdict(bool)

for command in commands:
    action, cubePositions = command.split(" ")
    positionRange = [[int(startEnd) for startEnd in position.split("=")[1].split("..")] for position in
                     cubePositions.split(",")]

    isOutOfPosition = False
    for position in positionRange:
        for value in position:
            if value < -50 or value > 50:
                isOutOfPosition = True
                break
        if isOutOfPosition:
            break
    if isOutOfPosition:
        continue

    for x in range(positionRange[0][0], positionRange[0][1] + 1, 1):
        for y in range(positionRange[1][0], positionRange[1][1] + 1, 1):
            for z in range(positionRange[2][0], positionRange[2][1] + 1, 1):
                # print(x, y, z)
                cubeDict[(x, y, z)] = True if action == "on" else False

nbOn = 0
for cube, value in cubeDict.items():
    if value:
        nbOn +=1
print("rs part1: ", nbOn)



## part2
with open('day22/day22_1_input.txt', 'r') as file:
    raw_data = file.read()


def parse_input(raw_data):
    res = []
    for line in raw_data.split('\n'):
        state = int(line.split()[0] == 'on')
        x0, x1, y0, y1, z0, z1 = map(int, re.findall('-?\d+', line))
        res.append((state, x0, x1, y0, y1, z0, z1))
    return res


DATA = parse_input(raw_data)
# print(DATA)


def intersect(cube_a, cube_b):
    x0, x1, y0, y1, z0, z1 = cube_a
    i0, i1, j0, j1, k0, k1 = cube_b
    x_s, y_s, z_s = (
        max(a, b) for a, b in
        zip((x0, y0, z0), (i0, j0, k0))
    )
    x_e, y_e, z_e = (
        min(a, b) for a, b in
        zip((x1, y1, z1), (i1, j1, k1))
    )
    # print(x_s, y_s, z_s, x_e, y_e, z_e)

    if x_s <= x_e and y_s <= y_e and z_s <= z_e:
        return x_s, x_e, y_s, y_e, z_s, z_e
    return False


def toggle_cubes(step, cubes):
    #print("step: ", step, "cubes: ", cubes)
    state, cur = step[0], step[1:]
    new = Counter()
    for cube in cubes:
        intsct = intersect(cur, cube)
        if intsct:
            print("intersect: ",intsct, "cube: ", cube, "cur: ", cur, cubes[cube])
            new[intsct] -= cubes[cube] ## if it is on substract 1 for intersection (prevents double checking)
            # print("new: ", new)
    if state:
        cubes[cur] = 1
    # print(new)
    cubes.update(new)
    print(cubes)
    print("--------------------------")
    return cubes


def calc_toggled(cubes):
    res = 0
    print("Calculation: ", cubes.items())
    for k, v in cubes.items():
        x0, x1, y0, y1, z0, z1 = k
        print(k)
        size = (x1 + 1 - x0) * (y1 + 1 - y0) * (z1 + 1 - z0)
        res += size * v
        print(res, v)
    return res


"""def part_one(steps):
    cubes = Counter()
    for step in steps:
        state, cur = step[0], step[1:]
        # print(cur)
        cur = intersect(cur, (-50, 50, -50, 50, -50, 50))
        if not cur:
            continue
        cubes = toggle_cubes((state, *cur), cubes)
    return calc_toggled(cubes)"""


def part_two(steps):
    cubes = Counter()
    for step in steps:
        cubes = toggle_cubes(step, cubes)
    return calc_toggled(cubes)

print("part2.", part_two(DATA))
