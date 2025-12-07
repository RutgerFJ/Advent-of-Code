def part_one(inp):
    total = 0

    for idx_y, line in enumerate(inp[:-1]):
        next_steps = []
        for idx_x, col in enumerate(line):
            if col == "|" or col == "S":
                next_steps.append((idx_x, idx_y + 1))

            for x, y in next_steps:
                if inp[y][x] == "^":
                    if any(char != "|" for char in [inp[y][x + 1], inp[y][x - 1]]):
                        total += 1
                    inp[y][x + 1] = "|"
                    inp[y][x - 1] = "|"
                else:
                    inp[y][x] = "|"

    return total


def part_two(inp):
    memo = {}
    height = len(inp)

    def traverse(x, y):
        if (x, y) in memo:
            return memo[(x, y)]

        if y >= height:
            return 1

        char = inp[y][x]
        if char == "^":
            num_paths = traverse(x - 1, y + 1) + traverse(x + 1, y + 1)
        else:
            num_paths = traverse(x, y + 1)

        memo[(x, y)] = num_paths
        return num_paths

    start_x = inp[0].index("S")
    return traverse(start_x, 0)


if __name__ == "__main__":
    with open("./2025/Day 7/input.txt", "r") as f:
        content = [list(line.strip()) for line in f]

    print(part_one(content))
    print(part_two(content))
