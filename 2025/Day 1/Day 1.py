def part_one(inp):
    dial = 50
    sum = 0

    for line in inp:
        direction = line[0]
        clicks = int(line[1::])

        dial += clicks if direction == "R" else -clicks
        dial %= 100

        if dial == 0:
            sum += 1

    return sum


def part_two(inp):
    dial = 50
    sum = 0

    for line in inp:
        direction = line[0]
        clicks = int(line[1::])

        for _ in range(abs(clicks)):
            dial += 1 if direction == "R" else -1
            if dial == 0:
                sum += 1
            elif dial == 100:
                dial = 0
                sum += 1
            elif dial == -1:
                dial = 99

    return sum


if __name__ == "__main__":
    with open("./2025/Day 1/input.txt", "r") as f:
        content = [line.strip() for line in f]

    print(part_one(content))
    print(part_two(content))
