def main():
    with open('input.txt', 'r') as f:
        content = [line.strip().split() for line in f]

    x_register = [1]
    for row in content:
        x_register.append(x_register[-1])
        if row[0] != 'noop':
            x_register.append(x_register[-1] + int(row[-1]))

    print(sum([x_register[cycle - 1] * cycle for cycle in range(20, 221, 40)]))


main()
