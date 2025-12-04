def check_surrounding_coords(grid, idx_y, idx_x):
    surrounding = 0

    if idx_x > 0:
        surrounding += 1 if grid[idx_y][idx_x - 1] == "@" else 0
    if idx_x < len(grid[idx_y]) - 1:
        surrounding += 1 if grid[idx_y][idx_x + 1] == "@" else 0

    if idx_y > 0:
        start = max(0, idx_x - 1)
        end = min(len(grid[idx_y - 1]), idx_x + 2)
        surrounding += sum(1 for char in grid[idx_y - 1][start:end] if char == "@")

    if idx_y < len(grid) - 1:
        start = max(0, idx_x - 1)
        end = min(len(grid[idx_y + 1]), idx_x + 2)
        surrounding += sum(1 for char in grid[idx_y + 1][start:end] if char == "@")

    return surrounding


def remove_toilet_rolls(grid, to_remove):
    for y, x in to_remove:
        grid[y] = grid[y][:x] + "x" + grid[y][x + 1 :]
    return grid


def part_one(inp):
    count = 0

    for idx_y, y in enumerate(inp):
        for idx_x, x in enumerate(y):
            if x == "@":
                surrounding = check_surrounding_coords(inp, idx_y, idx_x)
                if surrounding < 4:
                    count += 1

    return count


def part_two(inp):
    total = 0

    while True:
        to_remove = set()
        for idx_y, y in enumerate(inp):
            for idx_x, x in enumerate(y):
                if x == "@":
                    surrounding = check_surrounding_coords(inp, idx_y, idx_x)
                    if surrounding < 4:
                        to_remove.add((idx_y, idx_x))
                        total += 1

        if not to_remove:
            break

        inp = remove_toilet_rolls(inp, to_remove)

    return total


if __name__ == "__main__":
    with open("./2025/Day 4/input.txt", "r") as f:
        content = [line.strip() for line in f]

    print(part_one(content))
    print(part_two(content))
