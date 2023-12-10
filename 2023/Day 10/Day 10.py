def get_pipe_start(inp):
    for y, row in enumerate(inp):
        for x in range(len(row)):
            if inp[y][x] == 'S':
                return (y, x)


def get_move(char, direction, coord):
    moves = {
        '|N': (-1,  0, 'N'),
        '|S': ( 1,  0, 'S'),
        '-E': ( 0,  1, 'E'),
        '-W': ( 0, -1, 'W'),
        'LS': ( 0,  1, 'E'),
        'LW': (-1,  0, 'N'),
        'JS': ( 0, -1, 'W'),
        'JE': (-1,  0, 'N'),
        '7N': ( 0, -1, 'W'),
        '7E': ( 1,  0, 'S'),
        'FN': ( 0,  1, 'E'),
        'FW': ( 1,  0, 'S'),
        'SS': ( 0,  1, 'E'),
        'SN': (-1,  0, 'N'),
    }

    y, x, dir = moves[''.join([char, direction])]
    return ((coord[0] + y, coord[1] + x), dir)


def find_adjacent(row, y, x, pipe):
    return sum([1 for i, char in enumerate(row) 
                if i > x and char in 'SJL|' and (y, i) in pipe])


def map_pipe(inp):
    pipe, startpoint, direction = set(), get_pipe_start(inp), 'N'
    coord = startpoint

    while True:
        coord, direction = get_move(inp[coord[0]][coord[1]], direction, coord)
        pipe.add(coord)
        if coord == startpoint:
            break

    return pipe


def part_one(inp):
    return len(map_pipe(inp)) // 2


def part_two(inp):
    pipe = map_pipe(inp)
    enclosed = 0

    for y, row in enumerate(inp):
        for x in range(len(row)):
            if (y, x) not in pipe and find_adjacent(row, y, x, pipe) % 2 != 0:
                enclosed += 1

    return enclosed


def main():
    with open('./2023/Day 10/input.txt') as f:
        content = [line.strip() for line in f]

    print(part_one(content))
    print(part_two(content))


main()
