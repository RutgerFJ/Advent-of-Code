def part_one(inp):
    races = zip(map(int, inp[0]), map(int, inp[1]))

    ways = 1
    for time, dist in races:
        ways *= sum([1 for t in range(1, time) if t * (time - t) > dist])
    
    return ways


def part_two(inp):
    time = int(''.join(inp[0]))
    dist = int(''.join(inp[1]))

    return sum([1 for t in range(1, time) if t * (time - t) > dist])


if __name__ == '__main__':
    with open('./2023/Day 6/input.txt', 'r') as f:
        content = [line.split()[1:] for line in f]

    print(part_one(content))
    print(part_two(content))
