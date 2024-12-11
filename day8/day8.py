from collections import defaultdict
from itertools import permutations

from util.grid import on_grid
from util.tuple_arithmetics import tup_add, tup_sub

# input = 'example8.txt'
input = 'input8.txt'
data = [line.strip() for line in open(input).readlines()]


part1, part2 = set(), set()

antennas = defaultdict(list)
for l, line in enumerate(data):
    for c, char in enumerate(line):
        if char != '.':
            antennas[char].append((l, c))

for entry in antennas.values():
    print('entry', entry)
    for a, b in permutations(entry, 2):  # time saver!
        antinode = (tup_add(a, tup_sub(a, b)))
        if on_grid(antinode, data):
            part1.add(antinode)
    print(part1)

for entry in antennas.values():
    for a, b in permutations(entry, 2):
        distance = tup_sub(a, b)
        while distance[0] % 2 == 0 and distance[1] % 2 == 0:
            distance = (distance[0] / 2, distance[1] / 2)
        antinode = tup_add(a, distance)
        while on_grid(antinode, grid_size):
            part2.add(antinode)
            antinode = tup_add(antinode, distance)
        antinode = tup_sub(a, distance)
        while on_grid(antinode, grid_size):
            part2.add(antinode)
            antinode = tup_sub(antinode, distance)

print('part1: ', len(part1))
print('part2: ', len(part2))
