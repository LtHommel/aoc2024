from bisect import insort
from collections import defaultdict
from itertools import batched

# input = 'example9.txt'
input = 'input9.txt'
data = open(input).read().strip()

part1 = part2 = 0


def get_blocks():
    blocks = []
    files = []
    free_space = defaultdict(list)
    id = 0
    for batch in batched(data, 2):
        files.append((id, int(batch[0]), len(blocks)))
        for x in range(int(batch[0])):
            blocks.append(id)
        id += 1
        if len(batch) == 2:
            free_space[int(batch[1])].append(len(blocks))
            for x in range(int(batch[1])):
                blocks.append('.')
    free_space.pop(0)  # TODO wat doet die 0 daar überhaupt?
    return blocks, files, free_space


def move_blocks1(blocks):
    result = []
    reversed_block_index = -1
    file_count = len(blocks) - blocks.count('.')
    for i, block in enumerate(blocks):
        if i < file_count:
            if block == '.':
                while blocks[reversed_block_index] == '.':
                    reversed_block_index -= 1
                result.append(blocks[reversed_block_index])
                blocks[reversed_block_index] = '.'
            else:
                result.append(block)
    return result


def get_left_most_fit(free_space, size, index):
    left_most_fit = index
    found_size = 0
    found_index = -1
    for free_block_size in free_space:
        if free_block_size >= size:
            found_size = free_block_size
            found_index = free_space[free_block_size][0]
            if found_index < left_most_fit:
                left_most_fit = found_index


    # update free_space dict to reflect the situation after file move
    if found_size > 0:
        free_space[found_size].remove(found_index)
        if len(free_space[found_size]) == 0:
            free_space.pop(found_size)
        left_space = found_size - size
        if left_space > 0:
            insort(free_space[left_space], found_index + size)
    print('free_space post update', free_space.keys())
    return left_most_fit, free_space


def move_blocks2(blocks, files, free_space):
    print('blocks', blocks)
    print('free_space', free_space)
    result = blocks.copy()
    for id, size, index in reversed(files):
        print('\nfile', id, size, index)
        left_most_fit, free_space = get_left_most_fit(free_space, size, index)
        print('left_most_fit', left_most_fit)
        if index > left_most_fit:
            for i in range(size):
                result[index] = '.'
                index += 1
                result[left_most_fit] = id
                left_most_fit += 1
    return result


def checksum(blocks):
    # print('in checksum', blocks)
    result = 0
    for i, block in enumerate(blocks):
        if block != '.':
            result += i * int(block)
    return result


print('part1: ', checksum(move_blocks1(get_blocks()[0])))
# 15784310055226 too high
# 4020151813050 too low
print('part2: ', checksum(move_blocks2(*get_blocks())))
