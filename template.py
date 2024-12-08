input = 'example{day}.txt'
# input = 'input{day}.txt'
data = [line.strip() for line in open(input).readlines()]

part1 = part2 = 0

for line in data:
    # calculate solution

print('part1: ', part1)
print('part2: ', part2)
