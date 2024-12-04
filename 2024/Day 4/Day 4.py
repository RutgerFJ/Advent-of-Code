def find_xmas(x, x_max, y, y_max, content):
    count = 0
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]

    for dx, dy in directions:
        if 0 <= x + 3 * dx <= x_max and 0 <= y + 3 * dy <= y_max:
            if (
                content[y][x]
                + content[y + dy][x + dx]
                + content[y + 2 * dy][x + 2 * dx]
                + content[y + 3 * dy][x + 3 * dx]
                == "XMAS"
            ):
                count += 1
        if 0 <= x - 3 * dx <= x_max and 0 <= y - 3 * dy <= y_max:
            if (
                content[y][x]
                + content[y - dy][x - dx]
                + content[y - 2 * dy][x - 2 * dx]
                + content[y - 3 * dy][x - 3 * dx]
                == "XMAS"
            ):
                count += 1

    return count


def part_one(content):
    total = 0
    for y, line in enumerate(content):
        for x, char in enumerate(line):
            if char == "X":
                total += find_xmas(x, len(line) - 1, y, len(content) - 1, content)
    return total


def find_x_shaped_mas(x, y, content):
    if content[y + 1][x + 1] == "M" and content[y - 1][x - 1] == "M":
        return False
    if content[y + 1][x - 1] == "M" and content[y - 1][x + 1] == "M":
        return False
    if content[y + 1][x + 1] == "S" and content[y - 1][x - 1] == "S":
        return False
    if content[y + 1][x - 1] == "S" and content[y - 1][x + 1] == "S":
        return False

    letters = [
        content[y + 1][x + 1],
        content[y + 1][x - 1],
        content[y - 1][x + 1],
        content[y - 1][x - 1],
    ]

    if set(letters) == {"M", "S"}:
        return True

    return False


def part_two(content):
    total = 0
    for y, line in enumerate(content[1:-1], 1):
        for x, char in enumerate(line[1:-1], 1):
            if char == "A":
                total += find_x_shaped_mas(x, y, content)
    return total


if __name__ == "__main__":
    with open("./2024/Day 4/input.txt", "r") as f:
        content = [line.strip() for line in f]

    print(part_one(content))
    print(part_two(content))
