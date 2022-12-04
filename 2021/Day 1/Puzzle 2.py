def main():
    with open('input.txt', 'r') as f:
        content = [int(line.strip()) for line in f]

    increases = -1
    last = 0
    for x in range(len(content)):
        measurement = sum(content[x - 1:x + 2])
        if measurement > last:
            increases += 1
        last = measurement
    print(increases)


main()
