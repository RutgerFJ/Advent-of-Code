def main():
    with open('input.txt', 'r') as f:
        content = [line.strip().split() for line in f]

    cycle, x = 1, 1
    signal_strengths = []

    for line in content:
        cycle += 1
        if cycle % 40 == 20:
            signal_strengths.append(cycle * x)
        if len(line) > 1:
            cycle += 1
            x += int(line[1])
            if cycle % 40 == 20:
                signal_strengths.append(cycle * x)

    print(sum(signal_strengths))


main()
