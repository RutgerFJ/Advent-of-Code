def extrapolate(line, direction):
    deltas = [line[::direction]]

    while any(line):
        line = [line[x+1] - line[x] for x in range(len(line) - 1)]
        deltas.append(line[::direction])
    
    next = 0
    for seq in deltas[-2::-1]:
        next = seq[-1] + direction * next

    return next


def part_one(inp):
    return sum([extrapolate(line, 1) for line in inp])


def part_two(inp):
    return sum([extrapolate(line, -1) for line in inp])


def main():
    with open('input.txt', 'r') as f:
        content = [list(map(int, line.split())) for line in f]

    print(part_one(content))
    print(part_two(content))


main()
