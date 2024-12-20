import time
from collections import deque

from util.tuple_arithmetics import tup_add

t0 = time.time_ns()

# input = 'small_example15.txt'
input = 'small_example15p2.txt'
# input = 'example15.txt'
# input = 'input15.txt'
warehouse, moves = open(input).read().split('\n\n')

walls = set()
boxes = set()
position = ()

wide_walls = set()
big_boxes = set()
position2 = ()

for l, line in enumerate(warehouse.splitlines()):
    for c, char in enumerate(line):
        if char == '#':
            walls.add((l, c))
            wide_walls.add((l, c * 2))
            wide_walls.add((l, c * 2 + 1))
        elif char == 'O':
            boxes.add((l, c))
            big_boxes.add(((l, c * 2), 'l'))
            big_boxes.add(((l, c * 2 + 1), 'r'))
        elif char == '@':
            position = (l, c)
            position2 = (l, c * 2)

directions = {
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1),
}


# def part_1(position):
#     for move in moves:
#         if move not in directions:
#             continue
#
#         direction = directions[move]
#         next_position = tup_add(position, direction)
#         if next_position in walls:
#             continue
#
#         if next_position in boxes:
#             first_box_to_move = next_position
#             the_one_thereafter = tup_add(next_position, direction)
#             while the_one_thereafter in boxes:
#                 the_one_thereafter = tup_add(the_one_thereafter, direction)
#             if the_one_thereafter in walls:
#                 continue
#             else:
#                 boxes.add(the_one_thereafter)
#                 boxes.remove(first_box_to_move)
#         position = next_position
#
#     return sum([(100 * l) + c for l, c in boxes])


def list_comprehension_search(data, target):
    result = [tup for tup in data if target in tup]
    return result[0] if result else None


def get_next_level_boxes(current_level_boxes, direction):
    for box in current_level_boxes:
        if tup_add(box, direction) in wide_walls:
            None
        [list_comprehension_search(big_boxes, tup_add(box, direction)) for box in current_level_boxes]


def part_2(position2, wide_walls, big_boxes):
    for move in moves:
        if move not in directions:
            continue

        print('\nattempting to move', move, 'from', position2)
        print('boxes are here', big_boxes)

        direction = directions[move]
        next_position = tup_add(position2, direction)
        if next_position in wide_walls:
            print('found wall, stay put')
            continue

        if first_box := list_comprehension_search(big_boxes, next_position):
            print('found part of a box', first_box)
            if move == '<' or move == '>':
                boxes_to_move = [first_box]
                the_one_thereafter = tup_add(next_position, direction)
                while next_box := list_comprehension_search(big_boxes, the_one_thereafter):
                    print('found another part of a box', next_box)
                    boxes_to_move.append(next_box)
                    the_one_thereafter = tup_add(the_one_thereafter, direction)
                if the_one_thereafter in wide_walls:
                    print('found wall behind the boxes, stay put')
                    continue
                else:
                    move_big_boxes(boxes_to_move, direction)
            else:
                if to_move := find_big_boxes(direction, first_box):
                    move_big_boxes(to_move, direction)
                else:
                    continue

        print('moving to', next_position)
        position2 = next_position

    return sum([(100 * l) + c for l, c in [big_box[0] for big_box in big_boxes if big_box[1] == 'l']])


def find_big_boxes(direction, first_box_part):
    pos, part = first_box_part
    boxes_to_move = []
    current_level_boxes = deque([first_box_part])

    other_half_of_box = list_comprehension_search(big_boxes,
                                                  tup_add(pos, (0, 1) if part == 'l' else (0, -1)))
    print('found other half:', other_half_of_box)
    # boxes_to_move.append(other_half_of_box)
    current_level_boxes.append(other_half_of_box)

    while current_level_boxes:
        box_part = current_level_boxes.popleft()
        if box_part in boxes_to_move:
            continue

        boxes_to_move.append(box_part)
        next_position = tup_add(box_part[0], direction)
        if next_position in wide_walls:
            return None
        if next_box_part := list_comprehension_search(big_boxes, next_position):
            current_level_boxes.append(next_box_part)
            next_box_other_part = list_comprehension_search(big_boxes,
                                                  tup_add(next_box_part[0], (0, 1) if next_box_part[1] == 'l' else (0, -1)))
            current_level_boxes.append(next_box_other_part)

    print("let's move these:", boxes_to_move)
    return boxes_to_move


def move_big_boxes(boxes_to_move, direction):
    print("there's room behind the boxes: move them boxes!")
    for box in boxes_to_move:
        moved_box = (tup_add(box[0], direction), box[1])
        big_boxes.remove(box)
        big_boxes.add(moved_box)
    print('boxes are now here:', big_boxes)


# print('\npart1: ', part_1(position)) # 1456590
print('part2: ', part_2(position2, wide_walls, big_boxes))

t1 = time.time_ns()
print('en dat alles in een luttele', (t1 - t0) / 1000000, 'ms')
