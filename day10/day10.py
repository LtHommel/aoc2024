from collections import defaultdict, deque

from util.grid import get_grid_value, get_neighbors

# input = 'example10.txt'
input = 'input10.txt'
data = [[int(char) for char in line.strip()] for line in open(input).readlines()]

part1 = part2 = 0


def follow_trail1(trailhead):
    trail = deque([trailhead])
    visited = set()
    summits = 0

    while trail:
        step = trail.pop()
        if step in visited:
            continue
        visited.add(step)

        height = get_grid_value(step[1], step[0], data)
        if height == 9:
            summits += 1

        next_steps = get_neighbors(step, data)
        for next_step in next_steps:
            if get_grid_value(next_step[1], next_step[0], data) - height == 1:
                trail.append(next_step)
    return summits


def follow_trail2(trailhead):
    trail = deque([(trailhead, (trailhead,))]) # dit was eerst een lijst, maar dat geeft een error in r41: "TypeError: unhashable type: 'list'", hier een tuple van maken is kennelijk de oplossing, maar ik weet nog niet waarom
    visited = set()
    pathways = set()

    while trail:
        path = trail.pop()
        if path in visited:
            continue
        visited.add(path)

        step, pathway = path
        height = get_grid_value(step[1], step[0], data)
        if height == 9:
            pathways.add(pathway)

        next_steps = get_neighbors(step, data)
        for next_step in next_steps:
            if get_grid_value(next_step[1], next_step[0], data) - height == 1:
                trail.append((next_step, pathway + next_step))
    return len(pathways)


for l, line in enumerate(data):
    for c, x in enumerate(line):
        if x == 0:
            part1 += follow_trail1((l, c))
            part2 += follow_trail2((l, c))

print('part1: ', part1)
print('part2: ', part2)
