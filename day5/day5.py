from collections import defaultdict
from math import floor

# data = open('example5.txt').read()
data = open('input5.txt').read()

part1 = part2 = 0

rules, updates = data.split('\n\n')

# process rules
rule_dict = defaultdict(set) # Will return an empty set when accessing a non-existing key. Actually, it creates that key with an empty set as value, and it returns that.
for rule in rules.split('\n'):
    x, y = rule.split('|')
    rule_dict[int(x)].add(int(y))


def in_correct_order(items):
    seen = set()  # {} is een lege dictionary, geen lege set
    for n in items:
        intersection = seen & rule_dict[n]
        if intersection:
            return False, correct(items)
        seen.add(n)
    return True, items


def middle_item(items): # util nominee
    return items[floor(len(items) / 2)]


def correct(items):
    seen = set()
    reordered = items # TODO this is unsafe
    for n in items:
        intersection = seen & rule_dict[n]
        if intersection:
            i = reordered.index(n)
            prev = i - 1
            reordered[prev], reordered[i] = reordered[i], reordered[prev]
            correct(reordered)
        seen.add(n)
    return reordered


for update in updates.split('\n'):
    numbers = [int(x) for x in update.split(',')]
    is_original, correct_sequence = in_correct_order(numbers)
    if is_original:
        part1 += middle_item(correct_sequence)
    else:
        part2 += middle_item(correct_sequence)


print('part1: ', part1)
print('part2: ', part2)
