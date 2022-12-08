def check(tree, side):
    count = 0
    for i in side:
        if int(i) >= tree:
            count += 1
            break
        elif int(i) < tree:
            count += 1
    return count


def main():
    with open('input.txt', 'r') as file:
        content = [i.strip() for i in file]

    x, y = len(content[0]), len(content)
    scores = set()

    for row in range(1, y - 1):
        for column in range(1, x - 1):
            n = [content[x][column] for x in range(row - 1, -1, -1)]
            s = [content[x][column] for x in range(row + 1, y)]
            e = [content[row][x] for x in range(column + 1, x)]
            w = [content[row][x] for x in range(column - 1, -1, -1)]
            t = int(content[row][column])
            scores.add(check(t, n) * check(t, e) * check(t, s) * check(t, w))

    print(max(scores))


main()
