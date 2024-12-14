from util.grid import get_neighbors, get_surroundings
from util.tuple_arithmetics import tup_add

# input_file = 'example12.txt'
input_file = 'input12.txt'
data = [line.strip() for line in open(input_file)]

part1 = part2 = 0
seen = set()
regions = []


def find_region(pos):
    henk = data[pos[0]][pos[1]]
    region = [pos]
    seen.add(pos)

    for neighbor in get_neighbors(pos, data):
        if neighbor not in seen and data[neighbor[0]][neighbor[1]] == henk:
            region.extend(find_region(neighbor))

    return region


for l, line in enumerate(data):
    for c, char in enumerate(line):
        if (l, c) not in seen:
            regions.append(find_region((l, c)))


def neighboring_plots(x, plot):
    return (x[0] == plot[0] and abs(x[1] - plot[1]) == 1) or (x[1] == plot[1] and abs(x[0] - plot[0]) == 1)


def count_fences(region):
    return sum(4 - sum(1 for x in region if neighboring_plots(x, plot)) for plot in region)


def count_sides(region):
    corners = set()
    aidee = data[region[0][0]][region[0][1]]

    corner_positions = {
        'NE': ((-0.25, 0.25), [1, 4], [2]),
        'SE': ((0.25, 0.25), [4, 6], [7]),
        'SW': ((0.25, -0.25), [6, 3], [5]),
        'NW': ((-0.25, -0.25), [3, 1], [0])
    }

    for plot in region:
        surroundings = get_surroundings(plot[1], plot[0], data)

        for offset, outside_indices, inside_indices in corner_positions.values():
            if surroundings[outside_indices[0]] != aidee and surroundings[outside_indices[1]] != aidee:
                corners.add(tup_add(plot, offset))
            if all(surroundings[i] == aidee for i in outside_indices) and surroundings[inside_indices[0]] != aidee:
                corners.add(tup_add(plot, offset))

    return len(corners)


for region in regions:
    area = len(region)
    part1 += area * count_fences(region)
    part2 += area * count_sides(region)

print('part1:', part1)
print('part2:', part2)
