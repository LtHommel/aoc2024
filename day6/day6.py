from util.console import bcolors
from util.grid import get_surroundings
from util.grid import Direction

data = [line.strip('\n') for line in open('example6.txt').readlines()]
# data = [line.strip('\n') for line in open('input6.txt').readlines()]

part2 = 0


def get_direction(arrow):
    if arrow == '^':
        return Direction.UP
    elif arrow == '>':
        return Direction.RIGHT
    elif arrow == 'v':
        return Direction.DOWN
    elif arrow == '<':
        return Direction.LEFT
    else:
        raise ValueError


def get_starting_point():
    for i, line in enumerate(data):  # met enumerate() kun je de index gebruiken
        for arrow in ['^', '>', 'v', '<']:
            j = line.find(arrow)
            if j >= 0:
                return j, i, get_direction(arrow)


def next_position(current, direction):
    return tuple(map(lambda i, j: i + j, current, Direction.step_offset(direction)))


def what_if(current_pos, next_pos, direction):
    data[next_pos[1]][next_pos[0]] = '#'
    trail = set()

    x, y = next_position((current_pos[1], current_pos[0]), direction)
    next_step = data[y][x]

    while next_step is not None:
        if next_step == '#':
            # turn right
            direction = Direction.turn_right(direction)
        else:
            # move
            trail.add((r, c))
            c, r = move_guard(c, r, direction)

        next_step = get_surroundings(r, c, data)[direction.value]




    data[next_pos[1]][next_pos[0]] = '.'


def part_1(trail, r, c, direction):
    x, y = next_position((r, c), direction)
    next_step = data[y][x]

    while next_step is not None:
        if next_step == '#':
            # turn right
            direction = Direction.turn_right(direction)
        else:
            what_if((c, r), (x, y), direction)

            # move
            trail.add((r, c))
            print(f"{bcolors.WARNING}Step {len(trail)}: moving {direction}{bcolors.ENDC}")
            c, r = move_guard(c, r, direction)

        next_step = get_surroundings(r, c, data)[direction.value]

    trail.add((r, c))
    return trail


def move_guard(c, r, direction):
    offset_r, offset_c = Direction.step_offset(direction)
    r += offset_r
    c += offset_c
    return c, r


# door de * wordt de tuple geretourneerd door get_starting_point() 'uitgepakt' en worden de drie waarden als drie argumenten meegegeven aan move_guard()
final_trail = part_1(set(), *get_starting_point())

blocks = set()

# blocks.remove(get_starting_point()[0])
print('blocks', blocks)

print('part1: ', len(final_trail))
print('part2: ', len(blocks))

"""
3 obstakels + 1 punt uit de trail, zodanig dat ze een staggered vierkant vormen
        
      (x1,y1)
                (x3,y3)
(x0,y0)
        (x2,y2)
        
if not x0 + 1 == x1:
    continue
if not y0 + 1 == y2:
    continue
if not y1 + 1 == y3:
    continue
if not x2 + 1 == x3:
    continue

Niet gevonden, option 5:
....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
....|.|.#.
#..O+-+...
......#...

Omdat het geen vierkant is....

"""
