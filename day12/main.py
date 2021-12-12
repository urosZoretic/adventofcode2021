inputFile = "day12/day12_1_input.txt"

# https://adventofcode.com/2021/day/12

paths = set() # sets do not allow duplicates values so it is perfect :). we need uniq paths


def getPaths(graph, path):
    global paths
    if path[-1] == "end":
        # print("ONE path: ", path)
        paths.add(tuple(path))
        return
    # print("step: ",  graph[path[-1]])
    for g in graph[path[-1]]:
        if g.islower():
            if not g in path:  # lower paths should not be ore then once in path
                getPaths(graph, path + [g])
        else:
            getPaths(graph, path + [g])
    return


def getPaths2(graph, path, double):
    global paths
    if path[-1] == "end":
        # print("ONE path: ", path)
        paths.add(tuple(path))
        return
    # print("step: ",  graph[path[-1]], path, double)
    for g in graph[path[-1]]:
        if g.islower():
            if double == "" and g != "start":
                getPaths2(graph, path + [g], g)
                if not g in path: # at the start we do not have douple
                    getPaths2(graph, path + [g], "")
            elif double == g:
                if path.count(g) == 1: getPaths2(graph, path + [g], g)
            else:
                if not g in path:
                    getPaths2(graph, path + [g], double)
        else:
            getPaths2(graph, path + [g], double)
    return


if __name__ == '__main__':
    print("Passage Pathing")

    graph = {}

    with open(inputFile, "r") as f:
        inputPaths = f.read().split("\n")

    # create connected graph of paths
    for path in inputPaths:
        fromTo = path.split("-")
        # print(fromTo)
        if fromTo[0] in graph:
            graph[fromTo[0]].append(fromTo[1])
        else:
            graph[fromTo[0]] = [fromTo[1]]
        if fromTo[1] in graph:
            graph[fromTo[1]].append(fromTo[0])
        else:
            graph[fromTo[1]] = [fromTo[0]]

    # print("Graph: ", graph)
    # print(["start"][-1])
    # print(graph[["start"][-1]])
    getPaths(graph, ["start"])
    # print("Paths: ", paths)
    print("part1. Graphq traversal.. nb paths: ", len(paths))

    # print("part2: ")
    getPaths2(graph, ["start"], "")
    print("part2. Graphq traversal.. nb paths one small cave double: ", len(paths))