def main():
    with open('input.txt', 'r') as f:
        data = ''.join(line.strip('\n') for line in f)

    last_four = ''
    total_parsed = ''
    for char in data:
        total_parsed += char
        if len(last_four) < 4:
            last_four += char
        else:
            last_four = last_four[1:4] + char
        if len(last_four) == 4 and len(set(last_four)) == 4:
            break

    print(len(total_parsed))

main()
