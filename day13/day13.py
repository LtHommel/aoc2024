import re
import time
from itertools import batched

t0 = time.time_ns()

# input = 'example13.txt'
input = 'input13.txt'
data = [line.strip() for line in open(input).readlines()]

part1 = part2 = 0

pattern = re.compile(r'(\d+).*?(\d+)')
extract_digits = lambda s: (int((m := pattern.search(s)).group(1)), int(m.group(2)))


def solve_claw_machine(a_org, b_org, prize_org):
    # multiply everything with b
    a = (a_org[0] * b_org[1], a_org[1] * b_org[0])
    prize = (prize_org[0] * b_org[1], prize_org[1] * b_org[0])
    b = (b_org[0] * b_org[1], b_org[1] * b_org[0])

    # eliminate b
    a = a[0] - a[1]
    b = b[0] - b[1]
    prize = prize[0] - prize[1]

    # find a and b
    a = prize / a
    b = (prize_org[0] - (a_org[0] * a)) / b_org[0]

    # if a and b aren't ints, there was no solution
    if a.is_integer() and b.is_integer():
        return (int(a) * 3) + int(b)
    else:
        return 0


for a_str, b_str, prize_str, _ in batched(data, 4):
    a = extract_digits(a_str)
    b = extract_digits(b_str)
    prize = extract_digits(prize_str)

    part1 += solve_claw_machine(a, b, prize)

    prize = tuple([x + 10000000000000 for x in prize])
    part2 += solve_claw_machine(a, b, prize)

t1 = time.time_ns()

print('\n')
print('part1: ', part1)  # 35729
print('part2: ', part2)  # 88584689879723
print('en dat alles in een luttele', (t1 - t0) / 1000000, 'ms')
