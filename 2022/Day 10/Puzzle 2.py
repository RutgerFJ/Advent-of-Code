def main():
    with open('input.txt', 'r') as f:
        content = [line.strip().split() for line in f]

    x_register = [1]
    for row in content:
        x_register.append(x_register[-1])
        if row[0] != 'noop':
            x_register.append(x_register[-1] + int(row[-1]))

    screen = [["." for x in range(40)] for x in range(6)]
    for index in range(len(x_register)):
        row = index // 40
        column = index - (index // 40 * 40)
        if abs(column - x_register[index]) <= 1:
            screen[row][column] = "#"

    for row in screen:
        print(''.join(row))


main()
