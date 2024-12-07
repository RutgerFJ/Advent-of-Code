from re import findall


def add(left, right):
    return left + right


def multiply(left, right):
    return left * right


def concatenate(left, right):
    return int(str(left) + str(right))


def calculate_outcomes(outcomes, right, operators):
    return [op(num, right) for num in outcomes for op in operators]


def solve(operators):
    total = 0

    for line in content:
        outcome = line[0]
        possible_outcomes = [line[1]]
        numbers = line[2:]

        for op in operators:
            for num in numbers:
                possible_outcomes = calculate_outcomes(possible_outcomes, num, op)

            if outcome in possible_outcomes:
                total += outcome
                break

    return total


def part_one():
    return solve([(add, multiply)])


def part_two():
    return solve([(add, multiply, concatenate)])


with open("./2024/Day 7/input.txt") as file:
    content = [list(map(int, findall(r"\d+", line))) for line in file]

print(part_one())
print(part_two())
