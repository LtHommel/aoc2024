import re

# data = open('example3.txt').read()
data = open('input3.txt').read()

part1 = part2 = 0

regex = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
for x,y in regex.findall(data):
    part1 += int(x) * int(y)

# do = [0] + [match.end() for match in re.compile(r"(do)(?!n't)").finditer(data)] # Laat deze toch even staan vanwege de wijze les met het uitsluiten van de substring "n't". Het was alleen niet nodig omdat ik had moeten zoeken op do() en don't(), met haakjes, en ik heb dus een probleem opgelost dat ik helemaal niet had!
do = [0] + [match.end() for match in re.compile(r"do\(\)").finditer(data)]
dont = [match.start() for match in re.compile(r"don't\(\)").finditer(data)]

data_part2 = ''
enabled = True
for i in range(len(data)):
    if enabled:
      data_part2 += data[i]
    if i in do:
        enabled = True
    elif i in dont:
        enabled = False

for x,y in regex.findall(data_part2):
    part2 += int(x) * int(y)

print('part1: ', part1)
print('part2: ', part2)
