def main():
    with open('input.txt', 'r') as f:
        content = [x.strip().split(' ') for x in f]

    coords = [0, 0]
    for line in content:
        if line[0] == 'forward':
            coords[0] += int(line[1])
        elif line[0] == 'down':
            coords[1] += int(line[1])
        elif line[0] == 'up':
            coords[1] -= int(line[1])
    print(coords[0] * coords[1])


main()
