def main():
    with open('input.txt', 'r') as f:
        data = ''.join(line.strip('\n') for line in f)

    total_parsed = ''
    last_four = ''
    for char in data:
        total_parsed += char
        if len(last_four) < 14:
            last_four += char
        else:
            last_four = last_four[1:14] + char
        if len(last_four) == 14 and len(set(last_four)) == 14:
            break

    print(len(total_parsed))


main()
