def part_one(inp):
    left_list = [int(line.split()[0]) for line in inp]
    right_list = [int(line.split()[1]) for line in inp]

    left_list.sort()
    right_list.sort()

    return sum([abs(left_list[i] - right_list[i]) for i in range(len(left_list))])


def part_two(inp):
    left_list = [int(line.split()[0]) for line in inp]
    right_list = [int(line.split()[1]) for line in inp]

    return sum([num * right_list.count(num) for num in left_list])


if __name__ == "__main__":
    with open("./2024/Day 1/input.txt", "r") as f:
        content = [line.strip() for line in f]

    print(part_one(content))
    print(part_two(content))
