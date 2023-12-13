def check_mirror(mirror, smudges):
    total = 0

    for x in range(len(mirror) - 1):
        diff = 0
        for a, b in zip(mirror[x::-1], mirror[x+1:]):
            diff += sum([aa != bb for (aa, bb) in zip(a, b)])
        if diff == smudges:
            total += x + 1

    return total


def score_mirror(mirror, smudges):
    cols = ["".join([r[c] for r in mirror]) for c in range(len(mirror[0]))]
    
    return 100 * check_mirror(mirror, smudges) + check_mirror(cols, smudges)


def part_one(inp):
    return sum([score_mirror(mirror, 0) for mirror in inp])


def part_two(inp):
    return sum([score_mirror(mirror, 1) for mirror in inp])


if __name__ == '__main__':
    with open('./2023/Day 13/input.txt', 'r') as f:
        inp = [[r for r in inp.split("\n")] for inp in f.read().split("\n\n")]
    
    print(part_one(inp))
    print(part_two(inp))
