def to_dec(boolList):
    binaryNumber = ''
    for boolNumber in boolList:
        binaryNumber += str(int(boolNumber))

    return int(binaryNumber, 2)


class Image:
    def __init__(self, input_lines: list[str], padding):
        self._enhancement = [c == '#' for c in input_lines[0]]
        self._padding = padding + 1
        self._size = len(input_lines[2:]) + self._padding * 2
        self._image = [
            [
                input_lines[2:][x - self._padding][y - self._padding] == '#'
                if self._is_in_image(x, y)
                else False
                for y in range(self._size)
            ]
            for x in range(self._size)
        ]
        # self._print_image()

    def _print_image(self) -> None:
        for row in self._image:
            print(row)
        print()

    def _is_in_image(self, x, y) -> bool:
        return (
            self._padding <= x < self._size - self._padding and
            self._padding <= y < self._size - self._padding
        )

    def enhance(self) -> None:
        edge_bit = False
        while self._padding > 1:
            self._padding -= 1
            edge_bit = self._enhancement[edge_bit]
            self._image = [
                [
                    self._enhancement[to_dec([
                        self._image[x + kx][y + ky]
                        for kx in (-1, 0, 1)
                        for ky in (-1, 0, 1)
                    ])] if self._is_in_image(x, y) else edge_bit
                    for y in range(self._size)
                ]
                for x in range(self._size)
            ]
            # self._print_image()

    def num_light_pixels(self) -> int:
        return sum(b for row in self._image[1:-1] for b in row[1:-1])


def part1(input_lines: list[str]) -> int:
    img = Image(input_lines, 2)
    img.enhance()
    return img.num_light_pixels()


def part2(input_lines: list[str]) -> int:
    img = Image(input_lines, 50)
    img.enhance()
    return img.num_light_pixels()


print("Trench Map")
with open("day20/day20_1_input.txt", "r") as f:
    input = f.read().split("\n")


print("part1. Num lit pixels: ", part1(input))
print("part2. Num lit pixels: ", part2(input))