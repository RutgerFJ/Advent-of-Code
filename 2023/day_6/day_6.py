def part_one(inp):
    races = zip(map(int, inp[0]), map(int, inp[1]))

    ways = 1
    for r in races:
        time = r[0]
        dist = r[1]
        ways *= sum([1 for ms in range(1, time) if (ms * (time - ms)) > dist])
    
    return ways


def part_two(inp):
    time = int(''.join(inp[0]))
    dist = int(''.join(inp[1]))

    return sum([1 for t in range(1, time) if (t * (time - t)) > dist])


def main():
    with open('input.txt', 'r') as f:
        content = [line.split()[1:] for line in f]

    print(part_one(content))
    print(part_two(content))


main()
