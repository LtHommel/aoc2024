# data = open('example.txt').readlines()
data = open('input.txt').readlines()

left = []
right = []

for line in data:
    l,r = line.split() # default split on whitespace
    left.append(int(l))
    right.append(int(r))

left.sort()
right.sort()

#use the tuple() to display a readable version of the zip output:
# print(tuple(zip(left,right)))

part1 = part2 = 0
for l, r in zip(left, right):
    part1 += abs(l - r)
    part2 += l * right.count(l)

print(part1)
print(part2)
