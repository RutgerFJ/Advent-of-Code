import re


def part_one(inp):
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    total = 0

    for line in inp:
        matches = re.findall(pattern, line)

        for match in matches:
            match = match.strip("mul()")
            numbers = match.split(",")
            total += int(numbers[0]) * int(numbers[1])

    return total


def part_two(inp):
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    total = 0
    enabled = True

    for line in inp:
        segments = re.split(r"(do\(\)|don't\(\))", line)

        for segment in segments:
            if segment == "do()":
                enabled = True
            elif segment == "don't()":
                enabled = False
            elif enabled:
                matches = re.findall(pattern, segment)
                for match in matches:
                    nums = match[4:-1].split(",")
                    total += int(nums[0]) * int(nums[1])

    return total


if __name__ == "__main__":
    with open("./2024/Day 3/input.txt", "r") as f:
        content = [line.strip() for line in f]

    print(part_one(content))
    print(part_two(content))
