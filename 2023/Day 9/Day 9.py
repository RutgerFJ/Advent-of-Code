def extrapolate(line, direction):
    deltas = [line[::direction]]
    
    while any(line):
        line = [r - l for l, r in zip(line, line[1:])]
        deltas.append(line[::direction])

    result = 0
    for seq in reversed(deltas[:-1]):
        result = seq[-1] + direction * result

    return result


def part_one(inp):
    return sum([extrapolate(line, 1) for line in inp])


def part_two(inp):
    return sum([extrapolate(line, -1) for line in inp])


if __name__ == '__main__':
    with open('./2023/Day 9/input.txt', 'r') as f:
        content = [list(map(int, line.split())) for line in f]

    print(part_one(content))
    print(part_two(content))
