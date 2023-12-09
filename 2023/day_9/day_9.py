def extrapolate(line, forward):
    deltas = []

    while True:
        deltas.append(line)

        if all(char == 0 for char in line):
            break
        else:
            line = [line[x+1] - line[x] for x in range(len(line) - 1)]

    prev = 0
    next = 0
    for delta in deltas[-2::-1]:
        prev = delta[0] - prev
        next = next + delta[-1]
    
    return next if forward else prev


def part_one(inp):
    return sum([extrapolate(line, True) for line in inp])


def part_two(inp):
    return sum([extrapolate(line, False) for line in inp])


def main():
    with open('./AoC2023/Day 9/input.txt', 'r') as f:
        content = [list(map(int, line.split())) for line in f if not line.isspace()]

    print(part_one(content))
    print(part_two(content))


main()
