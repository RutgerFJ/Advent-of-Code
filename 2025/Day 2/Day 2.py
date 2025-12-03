import re


def part_one(inp):
    total = 0

    for range_str in inp[0].split(","):
        start, end = map(int, range_str.split("-"))

        for num in range(start, end + 1):
            num_str = str(num)
            mid = len(num_str) // 2
            if num_str[:mid] == num_str[mid:]:
                total += num

    return total


def part_two(inp):
    total = 0

    for range_str in inp[0].split(","):
        start, end = map(int, range_str.split("-"))

        for num in range(start, end + 1):
            if bool(re.fullmatch(r"(.+)\1+", str(num))):
                total += num

    return total


if __name__ == "__main__":
    with open("./2025/Day 2/input.txt", "r") as f:
        content = [line.strip() for line in f]

    print(part_one(content))
    print(part_two(content))
