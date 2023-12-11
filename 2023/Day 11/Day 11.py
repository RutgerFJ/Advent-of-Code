from itertools import combinations


def manhattan_path(a, b):
    x1, y1 = a
    x2, y2 = b
    x_diff = x2 - x1
    y_diff = y2 - y1
    x_offset = 1 if x_diff > 0 else -1 if x_diff < 0 else 0
    y_offset = 1 if y_diff > 0 else -1 if y_diff < 0 else 0

    path_coordinates = []
    while x1 != x2 or y1 != y2:
        if x1 != x2 and (y1 == y2 or abs(x_diff) <= abs(y_diff)):
            x1 += x_offset
        else:
            y1 += y_offset
        path_coordinates.append((x1, y1))

    return path_coordinates


def map_universe(inp):
    galaxies, expanded_y, expanded_x = [], [], []
    
    for y, row in enumerate(inp):
        if any(col != '.' for col in row):
            for x, col in enumerate(row):
                if col == '#':
                    galaxies.append((y, x))
                    continue
        else:
            expanded_y.append(y)

    for col in range(len(inp)):
        if all(inp[row][col] == '.' for row in range(len(inp))):
            expanded_x.append(col)
    
    return galaxies, expanded_x, expanded_y


def part_one_or_two(inp, expansion):
    galaxies, exp_x, exp_y = map_universe(inp)

    total = 0
    for a, b in combinations(galaxies, 2):
        path = manhattan_path(a, b)
        manhattan_dist = abs(a[0] - b[0]) + abs(a[1] - b[1])
        exp_dist = sum([expansion for y, x in path 
                        if y in exp_y or x in exp_x])
        total += manhattan_dist + exp_dist

    return total


if __name__ == '__main__':
    with open('./2023/Day 11/input.txt', 'r') as f:
        content = [line.strip() for line in f]
    
    print(part_one_or_two(content, 1))
    print(part_one_or_two(content, 999_999))
