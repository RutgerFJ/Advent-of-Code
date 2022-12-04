def main():
    with open('input.txt', 'r') as f:
        content = [x.strip().split(' ') for x in f]

    coords = [0, 0]
    aim = 0
    for line in content:
        if line[0] == 'forward':
            coords[0] += int(line[1])
            coords[1] += aim * int(line[1])
        elif line[0] == 'down':
            aim += int(line[1])
        elif line[0] == 'up':
            aim -= int(line[1])
    print(coords[0] * coords[1])


main()
