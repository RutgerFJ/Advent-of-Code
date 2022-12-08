def main():
    with open('input.txt', 'r') as file:
        content = [i.strip() for i in file]

    visible = 2 * (len(content) - 2 + len(content[0]))
    x, y = len(content[0]), len(content)

    for row in range(1, y - 1):
        for col in range(1, x - 1):
            n = [content[x][col] for x in range(row - 1, -1, -1)]
            s = [content[x][col] for x in range(row + 1, y)]
            e = [content[row][x] for x in range(col + 1, x)]
            w = [content[row][x] for x in range(col - 1, -1, -1)]
            if content[row][col] > max(n) or content[row][col] > max(w) or \
               content[row][col] > max(s) or content[row][col] > max(e):
                visible += 1

    print(visible)


main()
