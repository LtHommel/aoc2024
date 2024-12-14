import math
import re
import time
from collections import defaultdict

t0 = time.time_ns()

# grid_x = 11
# grid_y = 7
# input = 'example14.txt'
input = 'input14.txt'
grid_x = 101
grid_y = 103
data = [line.strip() for line in open(input).readlines()]

part1 = part2 = 0

robots = defaultdict(int)

for line in data:
    px, py, vx, vy = map(int, re.findall(r'-?\d+', line))
    pos = (((vx * 100) + px) % grid_x, ((vy * 100) + py) % grid_y)
    robots[pos] += 1


def count_robots():
    quadrants = [0] * 4
    x_midline = grid_x // 2
    y_midline = grid_y // 2
    for pos in robots:
        if pos[0] < x_midline and pos[1] < y_midline:
            quadrants[0] += robots[pos]
        elif pos[0] > x_midline and pos[1] < y_midline:
            quadrants[1] += robots[pos]
        elif pos[0] < x_midline and pos[1] > y_midline:
            quadrants[2] += robots[pos]
        elif pos[0] > x_midline and pos[1] > y_midline:
            quadrants[3] += robots[pos]
    return quadrants

def get_safety_number():
    return math.prod(count_robots())

t1 = time.time_ns()

print('part1: ', get_safety_number()) # 219150360
print('part2: ', part2)
print('en dat alles in een luttele', (t1 - t0) / 1000000, 'ms')
