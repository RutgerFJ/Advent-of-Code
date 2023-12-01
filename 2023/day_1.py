def part_one(inp):
    file_digits = []

    for line in inp:
        line_digits = ''.join([i for i in line if i.isdigit()])
        getal = f'{line_digits[0]}{line_digits[-1]}'
        file_digits.append(int(getal))

    return sum(file_digits)


def part_two(inp):
    digit_dict = {
        "one": '1',
        "two": '2',
        "three": '3',
        "four": '4',
        "five": '5',
        "six": '6',
        "seven": '7',
        "eight": '8',
        "nine": '9'
    }

    file_digits = []

    for line in inp:
        line_digits = ''

        for i, char in enumerate(line):
            if char.isdigit():
                line_digits += char

            for word in digit_dict:
                if word == line[i:i+len(word)]:
                    line_digits += digit_dict[word]

        file_digits.append(int(f'{line_digits[0]}{line_digits[-1]}'))

    return sum(file_digits)


def main():
    with open('input.txt', 'r') as f:
        content = [line.strip() for line in f]
    
    print(part_one(content))
    print(part_two(content))


main()
