def check_safety(line):
    starting_number = line[0]
    increasing = True if line[1] > starting_number else False
    for x, num in enumerate(line):
        if x == 0:
            continue

        if increasing and not line[x] > line[x - 1]:
            return False

        elif not increasing and not line[x] < line[x - 1]:
            return False

        if not 1 <= abs(line[x] - line[x - 1]) <= 3:
            return False

    return True


def part_one(inp):
    safe_report_count = 0
    for line in inp:
        line = [int(num) for num in line.split()]

        if check_safety(line):
            safe_report_count += 1

    return safe_report_count


def part_two(inp):
    safe_report_count = 0
    for line in inp:
        line = [int(num) for num in line.split()]

        if any([check_safety(line[:i] + line[i + 1 :]) for i in range(len(line))]):
            safe_report_count += 1

    return safe_report_count


if __name__ == "__main__":
    with open("./2024/Day 2/input.txt", "r") as f:
        content = [line.strip() for line in f]

    print(part_one(content))
    print(part_two(content))
