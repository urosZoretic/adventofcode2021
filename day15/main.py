import sys
from dataclasses import dataclass
from heapq import heappush, heappop

with open('day15/day15_1_input.txt') as fh:
    data = fh.read()

def printData(g):
    for key in g:
        print(key, g[key])

@dataclass
class Pt:
    x: int
    y: int
    weight: int
    graph: dict

    total = sys.maxsize
    prev = None

    def __lt__(self, other):
        return self.total < other.total

    def __eq__(self, other):
        return self.total == other.total

    def __repr__(self):
        return 'Pt(x=%s, y=%s, weight=%s, total=%s, prev=%s)' % (
        self.x, self.y, self.weight, self.total, self.prevcoord)

    @property
    def coord(self):
        return (self.x, self.y)

    @property
    def prevcoord(self):
        if self.prev is not None:
            return self.prev.coord

    @property
    def neighbors(self):
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            try:
                yield self.graph[(self.x + dx, self.y + dy)]
            except KeyError:
                pass


def load_data(data):
    g = {}
    for y, line in enumerate(data.split()):
        for x, c in enumerate(line):
            g[(x, y)] = Pt(x, y, int(c), g)
    return g


def dijkstra(start):
    start.total = 0
    q = []
    visited = set()
    heappush(q, start)
    visited.add(start.coord)
    while q:
        current = heappop(q)
        # print("iteration")
        for node in current.neighbors:
            # print(node)
            if current.total + node.weight < node.total:
                node.prev = current
                node.total = node.weight + current.total
            if node.coord not in visited:
                heappush(q, node)
                visited.add(node.coord)
        # print(q)


g = load_data(data)

#printData(g)
# print(min(g))
# print(g[min(g)])


dijkstra(g[min(g)])

print('part_1 =', g[max(g)].total)


# Part 2

def wrap9(n):
    while n > 9:
        n -= 9
    return n


def expand5x(g):
    xmax, ymax = max(g)
    tilewidth, tileheight = xmax + 1, ymax + 1
    for pt in list(g.values()):
        for d in range(1, 5):
            newpt = Pt(pt.x + (d * tilewidth), pt.y, wrap9(pt.weight + d), g)
            g[(newpt.x, newpt.y)] = newpt
    for pt in list(g.values()):
        for d in range(1, 5):
            newpt = Pt(pt.x, pt.y + (d * tileheight), wrap9(pt.weight + d), g)
            g[(newpt.x, newpt.y)] = newpt


g = load_data(data)
expand5x(g)
dijkstra(g[min(g)])

print('part_2 =', g[max(g)].total)
