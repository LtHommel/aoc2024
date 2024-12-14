import time
from functools import cache
from math import floor, log10

t0 = time.time_ns()

# input = 'example11.txt'
input = 'input11.txt'
data = map(int, open(input).read().split())


@cache  # <- feest!
def blink(stone, blinks=25):
    if blinks == 0:
        return 1

    if stone == 0:
        return blink(1, blinks - 1)

    # De Jan-way:
    digits = floor(log10(stone)) + 1
    if 0 == digits % 2:
        split_base = 10 ** (digits // 2)
        return (blink(stone // split_base, blinks - 1) +
                blink(stone % split_base, blinks - 1))

    return blink(stone * 2024, blinks - 1)


part1 = sum([blink(stone, 25) for stone in data])
part2 = sum([blink(stone, 75) for stone in data])
# for stone in data:
#     part1 += blink(stone, 25)
#     part2 += blink(stone, 75)

t1 = time.time_ns()

print('part1: ', part1)
print('part2: ', part2)
print('en dat alles in een luttele', (t1 - t0) / 1000000, 'ms')
