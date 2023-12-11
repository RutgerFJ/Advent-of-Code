def initiate_pipe(inp):
    for y, row in enumerate(inp):
        if row.find('S') != -1:
            return set(), (y, row.index('S'))


def get_move(char, direction, row, col):
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
        'SS': ( 0,  1, 'E'), # hardcoded & input-specific
        'SW': (-1,  0, 'N')  # hardcoded & input-specific
    }
    y, x, dir = moves[char + direction]
    return row + y, col + x, dir


def find_adjacent(row, y, x, pipe):
    return sum([1 for i, char in enumerate(row) 
                if i > x and char in '|SJL' # '|SJL' and '|S7F' are both valid
                and (y, i) in pipe])


def map_pipe(inp):
    pipe, startpoint = initiate_pipe(inp)
    row, col = startpoint
    direction = 'W' # hardcoded & input-specific

    while True:
        row, col, direction = get_move(inp[row][col], direction, row, col)
        pipe.add((row, col))
        if (row, col) == startpoint:
            break

    return pipe


def part_one(inp):
    return len(map_pipe(inp)) // 2


def part_two(inp):
    pipe = map_pipe(inp)
    enclosed = 0
    for y, row in enumerate(inp):
        enclosed += sum([1 for x in range(len(row)) 
                         if (y, x) not in pipe and 
                         find_adjacent(row, y, x, pipe) % 2 != 0])

    return enclosed


if __name__ == '__main__':
    with open('./2023/Day 10/input.txt') as f:
        content = [line.strip() for line in f]

    print(part_one(content))
    print(part_two(content))
