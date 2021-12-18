# code from https://raw.githubusercontent.com/busdriverbuddha/aoc2021/main/day18.py  --> ta je ********

class Node:

    def __init__(self, s, parent=None):
        self.value = None
        self.left = None
        self.right = None
        self.parent = parent

        if "[" not in s:
            self.value = int(s)
        else:
            sub_s = s[1:-1]
            k = self._get_matching(sub_s)
            # print("k: ", k)
            if k is None:
                left, right = sub_s.split(",", 1)
                self.left = Node(left, self)
                self.right = Node(right, self)
            else:
                self.left = Node(sub_s[:k], self)
                self.right = Node(sub_s[k + 1:], self)

        # print("s", s, "parent: ", parent, "left: ", self.left, "right: ", self.right)

    def _get_matching(self, s):
        S = [s[0]]
        for i, c in enumerate(s[1:], 1):
            if c == "[":
                S.append(c)
            elif c == "]":
                S.pop()
            if len(S) == 0:
                return i + 1

    def __repr__(self):
        if self.value is not None:
            return f"Node({self.value})"

        return f"Node({self})"

    def __str__(self):
        if self.value is not None:
            return str(self.value)

        return f"[{self.left},{self.right}]"

    def add(self, other):
        n = Node(f"[{self},{other}]")
        # print("addding: ", n)
        n.reduce()
        return n

    def find_rightmost(self):
        if self.right is None:
            return self
        return self.right.find_rightmost()

    def find_leftmost(self):
        if self.left is None:
            return self
        return self.left.find_leftmost()

    def find_root(self):
        if self.parent is None:
            return self

        p = self.parent
        while p.parent is not None:
            p = p.parent
        return p

    def find_left_neighbor(self):
        if self.parent is None:
            return None

        if self.find_root().find_leftmost() == self:
            return None

        if self.parent.left != self:
            return self.parent.left.find_rightmost()

        # go up until you can go down left
        prev = self
        p = self.parent
        while True:
            if p.left != prev:
                break
            prev = p
            p = p.parent
        return p.left.find_rightmost()

    def find_right_neighbor(self):
        if self.parent is None:
            return None

        if self.find_root().find_rightmost() == self:
            return None

        if self.parent.right != self:
            return self.parent.right.find_leftmost()

        # go up until you can go down left
        prev = self
        p = self.parent
        while True:
            if p.right != prev:
                break
            prev = p
            p = p.parent
        return p.right.find_leftmost()

    def find_explodable(self, n=0):
        if n == 4 and self.value is None:
            return self

        left_result = right_result = None
        if self.left is not None:
            left_result = self.left.find_explodable(n + 1)

        if left_result is not None:
            return left_result

        if self.right is not None:
            right_result = self.right.find_explodable(n + 1)

        if right_result is not None:
            return right_result

    def find_ten(self):

        if self.value is not None and self.value >= 10:
            return self

        if self.value is not None:  # has value but not 10 or greater
            return None

        left_result = self.left.find_ten()
        if left_result is not None:
            return left_result

        right_result = self.right.find_ten()
        if right_result is not None:
            return right_result

    def split(self):
        if (n := self.find_ten()) is None:
            return False

        n.left = Node(str(n.value // 2), parent=n)
        n.right = Node(str(n.value - n.left.value), parent=n)
        n.value = None

        return True

    def explode(self):
        pair = self.find_explodable()
        if pair is None:
            return False

        left_neighbor = pair.left.find_left_neighbor()
        if left_neighbor is not None:
            left_neighbor.value += pair.left.value

        right_neighbor = pair.right.find_right_neighbor()
        if right_neighbor is not None:
            right_neighbor.value += pair.right.value

        pair.left = pair.right = None
        pair.value = 0

        return True

    def reduce(self):
        done = False
        while not done:
            done = True
            if self.explode():
                done = False
            elif self.split():
                done = False

    def magnitude(self):
        total = 0

        if self.left.value is not None:
            total += 3 * self.left.value
        else:
            total += 3 * self.left.magnitude()

        if self.right.value is not None:
            total += 2 * self.right.value
        else:
            total += 2 * self.right.magnitude()

        return total


# part 1

lines = [l.strip() for l in open("day18/day18_1_input.txt").readlines()]
# print(lines)

n = Node(lines[0])
# print(n)

for line in lines[1:]:
    n = n.add(Node(line))
    # print(n)

print(n.magnitude())

# part 2

max_magnitude = -1e9

for i, line1 in enumerate(lines):
    for j, line2 in enumerate(lines):
        if i != j:
            n = Node(line1).add(Node(line2))
            if (m := n.magnitude()) > max_magnitude:
                max_magnitude = m

print(max_magnitude)