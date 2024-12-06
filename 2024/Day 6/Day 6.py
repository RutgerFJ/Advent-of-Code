def find_start_pos():
    for pos, value in GRID.items():
        if value == "^":
            return pos


def move_guard(grid, pos, dy, dx):
    while True:
        new_pos = (pos[0] + dy, pos[1] + dx)

        if grid.get(new_pos) == "#":
            dy, dx = dx, -dy
        else:
            return new_pos, dy, dx


def find_route():
    visited = set()
    pos = find_start_pos()
    dy, dx = -1, 0

    while pos in GRID:
        visited.add(pos)
        pos, dy, dx = move_guard(GRID, pos, dy, dx)

    return visited


def find_loop(test_grid):
    visited = set()
    pos = find_start_pos()
    dy, dx = -1, 0

    while pos in test_grid:
        if (pos, dy, dx) in visited:
            return True

        visited.add((pos, dy, dx))
        pos, dy, dx = move_guard(test_grid, pos, dy, dx)

    return False


def part_one():
    return len(find_route())


def part_two():
    loop_count = 0

    for pos in find_route():
        test_grid = GRID.copy()
        test_grid[pos] = "#"
        loop_count += find_loop(test_grid)

    return loop_count


with open("./2024/Day 6/input.txt", "r") as f:
    content = [line.strip() for line in f]

GRID = {(y, x): char for y, line in enumerate(content) for x, char in enumerate(line)}

print(part_one())
print(part_two())
