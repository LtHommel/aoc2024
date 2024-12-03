# data = open('example2.txt').readlines()
data = open('input2.txt').readlines()

def safe(report):
    delta = []
    for x, y in zip(report, report[1:]):
        delta.append(x - y)
    if (all(1 <= abs(d) <= 3 for d in delta) # all() + generator expression (list comprehension zonder []) is superkrachtig en leesbaar!
            and (all(d > 0 for d in delta) or all(d < 0 for d in delta))):
        return True


def safe_afterall(report):
    for i in range(len(report)):
        if safe(report[:i] + report[i + 1:]): # list slicing! Lijst[beginindex:eindindex] begin en eind kun je leeg laten voor eerste of laatste item
            return True


part1 = part2 = 0

for line in data:
    report = [int(n) for n in line.split()]
    if safe(report):
        part1 += 1
        part2 += 1
    elif safe_afterall(report):
        part2 += 1

print('part1: ', part1)
print('part2: ', part2)
