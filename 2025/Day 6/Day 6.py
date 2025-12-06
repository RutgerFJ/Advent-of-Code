from math import prod


def part_one(inp):
    operators = inp[-1]
    total = 0

    for x in range(len(operators)):
        numbers = [int(inp[y][x]) for y in range(len(inp) - 1)]
        total += sum(numbers) if operators[x] == "+" else prod(numbers)

    return total


def part_two(inp):
    numbers = []
    total = 0

    for x in range(len(inp[0]))[::-1]:
        column = "".join(inp[y][x] for y in range(len(inp))).strip()

        if not column:
            numbers = []
            continue
        elif not column[-1].isdigit():
            numbers.append(int(column[:-1]))
            total += sum(numbers) if column[-1] == "+" else prod(numbers)
        else:
            numbers.append(int(column))

    return total


if __name__ == "__main__":
    with open("./2025/Day 6/input.txt", "r") as f:
        content_one = [line.strip().split() for line in f]

    print(part_one(content_one))

    with open("./2025/Day 6/input.txt", "r") as f:
        content_two = [line.strip("\n") for line in f]

    print(part_two(content_two))
