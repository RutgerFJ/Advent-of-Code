def main():
    with open('input.txt', 'r') as f:
        content = [int(line.strip()) for line in f]

    increases = -1
    last = 0
    for line in content:
        if line > last:
            increases += 1
        last = line
    print(increases)


main()
