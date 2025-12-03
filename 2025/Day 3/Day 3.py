def part_one(inp):
    total = 0

    for bank in inp:
        first_digit = max(map(int, bank[:-1]))
        index_first_digit = bank[:-1].index(str(first_digit))

        second_digit = max(map(int, bank[index_first_digit + 1 :]))

        combined = int(str(first_digit) + str(second_digit))
        total += combined

    return total


def part_two(inp):
    total = 0

    for bank in inp:
        digits = [int(d) for d in bank]

        selected_digits = []
        start = 0

        for _ in range(12):
            end = len(digits) - (12 - len(selected_digits)) + 1
            remaining_digits = digits[start:end]

            max_digit = max(remaining_digits)
            selected_digits.append(max_digit)

            start += remaining_digits.index(max_digit) + 1

        combined = int("".join(map(str, selected_digits)))
        total += combined

    return total


if __name__ == "__main__":
    with open("./2025/Day 3/input.txt", "r") as f:
        content = [line.strip() for line in f]

    print(part_one(content))
    print(part_two(content))
