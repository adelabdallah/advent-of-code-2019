from collections import defaultdict

# Part 1

planets = defaultdict(list)

with open('./day6/input.txt') as _file:
    for line in _file.readlines():
        planet, satellite = line.strip().split(')')
        planets[planet].append(satellite)


def orbitCount(node, count, total):
    total += count
    for satellite in planets[node]:
        total = orbitCount(satellite, count + 1, total)
    return total


print(orbitCount('COM', 0, 0))

# Part 2

nodes = defaultdict(list)

with open('./day6/input.txt') as _file:
    for line in _file.readlines():
        previous, _next = line.strip().split(')')
        nodes[previous].append(_next)
        nodes[_next].append(previous)

        if _next == "YOU":
            start = previous
        if _next == "SAN":
            target = previous

visitedNodes = set()

def traverse(node, count):
    visitedNodes.add(node)

    if node == target:
        print(count)
        return True
    for nextNode in nodes[node]:
        if nextNode in visitedNodes:
            continue
        if traverse(nextNode, count + 1):
            return True

traverse(start, 0)
