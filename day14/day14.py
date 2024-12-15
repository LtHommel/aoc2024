import math
import re
import sys
import time
from collections import defaultdict
from functools import lru_cache
from linecache import cache

t0 = time.time_ns()

# grid_x = 11
# grid_y = 7
# input = 'example14.txt'
input = 'input14.txt'
grid_x = 101
grid_y = 103
data = [line.strip() for line in open(input).readlines()]

robots = [tuple(map(int, re.findall(r'-?\d+', line))) for line in data]

def step(robot, t=100):
    px, py, vx, vy = robot
    return ((vx * t) + px) % grid_x, ((vy * t) + py) % grid_y


def safety_count(pos_count):
    quadrants = [0] * 4
    x_midline = grid_x // 2
    y_midline = grid_y // 2
    for pos, count in pos_count.items():
        x, y = pos
        if x < x_midline:
            quadrants[0 if y < y_midline else 2] += count
        else:
            quadrants[1 if y < y_midline else 3] += count
    return math.prod(quadrants)


def part_1():
    positions = defaultdict(int)
    for robot in robots:
        position = step(robot)
        positions[position] += 1
    return safety_count(positions)


def part_2():
    minimum_safety_count = sys.maxsize
    registered = 0
    positions = defaultdict(int)
    for second in range(grid_x * grid_y):
        positions.clear()
        for robot in robots:
            position = step(robot, second)
            positions[position] += 1
        if (sc := safety_count(positions)) < minimum_safety_count:
            minimum_safety_count = sc
            registered = second
    return registered


def show(t):
    positions = set()

    for robot in robots:
        position = step(robot, t)
        positions.add(position)

    draw_me = [[' ' for _ in range(grid_x)] for _ in range(grid_y)]

    for x, y in positions:
        draw_me[int(y)][int(x)] = 'x'

    for line in draw_me:
        print(" ".join(line))


part2 = part_2()

print('part1: ', part_1())  # 219150360
print('part2: ', part2)  # 8053
show(part2)

t1 = time.time_ns()
print('en dat alles in een luttele', (t1 - t0) / 1000000, 'ms')
