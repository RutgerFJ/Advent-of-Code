def part_one(inp):
    ranges = []
    ingredient_ids = []

    for line in inp:
        if "-" in line:
            ranges.append(range(int(line.split("-")[0]), int(line.split("-")[1]) + 1))
        elif line != "":
            ingredient_ids.append(int(line))

    return sum(
        1 for id in ingredient_ids if any(id in fresh_range for fresh_range in ranges)
    )


def merge_ranges(range_1, range_2):
    if range_1.stop < range_2.start or range_2.stop < range_1.start:
        return None
    else:
        return range(min(range_1.start, range_2.start), max(range_1.stop, range_2.stop))


def part_two(inp):
    ranges = []
    for line in inp:
        if "-" in line:
            start, end = map(int, line.split("-"))
            ranges.append(range(start, end + 1))

    while True:
        merged_any = False
        merged_ranges = []

        for i, current_range in enumerate(ranges):
            for j in range(i + 1, len(ranges)):
                merged = merge_ranges(current_range, ranges[j])
                if merged:
                    current_range = merged
                    ranges[j] = None
                    merged_any = True

            if current_range is not None:
                merged_ranges.append(current_range)

        ranges = [r for r in merged_ranges if r is not None]

        if not merged_any:
            break

    return sum(len(r) for r in ranges)


if __name__ == "__main__":
    with open("./2025/Day 5/input.txt", "r") as f:
        content = [line.strip() for line in f]

    print(part_one(content))
    print(part_two(content))
