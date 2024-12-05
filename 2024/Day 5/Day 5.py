def part_one(rules, updates):
    total = 0

    for up in updates:
        valid = True

        for rule in rules:
            if all(x in up for x in rule):
                if up.index(rule[0]) > up.index(rule[1]):
                    valid = False

        if valid:
            middle = int(len(up) / 2)
            total += up[middle]

    return total


def fix_order(up, rules):
    for _ in range(10):  # Not very proud of this one
        for rule in rules:
            if all(x in up for x in rule):
                if up.index(rule[0]) > up.index(rule[1]):
                    up[up.index(rule[0])], up[up.index(rule[1])] = (
                        up[up.index(rule[1])],
                        up[up.index(rule[0])],
                    )

    return up


def part_two(rules, updates):
    total = 0

    for up in updates:
        valid = True

        for rule in rules:
            if all(x in up for x in rule):
                if up.index(rule[0]) > up.index(rule[1]):
                    valid = False

        if not valid:
            fixed_up = fix_order(up, rules)
            middle = int(len(fixed_up) / 2)
            total += fixed_up[middle]

    return total


if __name__ == "__main__":
    rules = []
    updates = []

    with open("./2024/Day 5/input.txt", "r") as f:
        for line in f:
            if "|" in line:
                rules.append([int(x) for x in line.strip().split("|")])
            if "," in line:
                updates.append([int(x) for x in line.strip().split(",")])

    print(part_one(rules, updates))
    print(part_two(rules, updates))
