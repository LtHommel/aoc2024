data = open('example4.txt').readlines()
# data = open('input4.txt').readlines()

part1 = part2 = 0

data = [line.strip('\n') for line in data] # verwijder newlines

# diagonalen zoeken keihard gejat van https://stackoverflow.com/a/43311126/7920259
num_cols = len(data[0])
num_rows = len(data)
cols = ['' for _ in range(num_cols)]
rows = ['' for _ in range(num_rows)]
fw_diagonals = ['' for _ in range(num_rows + num_cols - 1)] # je kunt een _ gebruiken in plaats van een variabelenaam als je er niet meer naar refereert
bw_diagonals = ['' for _ in range(len(fw_diagonals))]
offset_bw_diagonals = -num_rows + 1

for x in range(num_cols):
    for y in range(num_rows):
        cols[x] += data[y][x]
        rows[y] += data[y][x]
        fw_diagonals[x + y] += data[y][x]
        bw_diagonals[x - y - offset_bw_diagonals] += data[y][x]

for strings in cols, rows, fw_diagonals, bw_diagonals:
    for string in strings:
        part1 += string.count('XMAS')
        part1 += string.count('SAMX')

# ------------ part 2 -----------------

# TODO

print('part1: ', part1)
print('part2: ', part2)
