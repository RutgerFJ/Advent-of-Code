from itertools import combinations


def manhattan_parser(a, b, x1, y1, x2, y2):
    path_coordinates = []

    for x in range(x1, x2, 1 if x2 > x1 else -1):
        path_coordinates.append((x, y1))

    for y in range(y1, y2, 1 if y2 > y1 else -1):
        path_coordinates.append((x2, y))

    distance = abs(a[0] - b[0]) + abs(a[1] - b[1])

    return path_coordinates, distance


def part_one_or_two(inp, expansion):
    galaxies = [(y, x) for y, row in enumerate(inp) 
                for x, col in enumerate(row) if col == '#']
    
    exp_y = [row for row in range(len(inp))
             if all(inp[row][col] == '.' for col in range(len(inp)))]
    
    exp_x = [col for col in range(len(inp)) 
             if all(inp[row][col] == '.' for row in range(len(inp)))]

    return sum(manh_dist + sum([expansion for y, x in path if y in exp_y or x in exp_x])
               for a, b in combinations(galaxies, 2)
               for path, manh_dist in [manhattan_parser(a, b, *a, *b)])


if __name__ == '__main__':
    with open('./2023/Day 11/input.txt', 'r') as f:
        content = [line.strip() for line in f]
    
    print(part_one_or_two(content, 1))
    print(part_one_or_two(content, 999_999))