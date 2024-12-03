import re

# data = open('example3.txt').read()
data = open('input3.txt').read()

part1 = part2 = 0

regex = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
for x,y in regex.findall(data):
    part1 += int(x) * int(y)

enabled = True
for do, dont, x, y in re.findall(r'(do\(\))|(don\'t\(\))|mul\((\d{1,3}),(\d{1,3})\)', data):
    if do:
        enabled = True
    elif dont:
        enabled = False
    elif enabled:
        part2 += int(x) * int(y)

print('part1: ', part1)
print('part2: ', part2)
