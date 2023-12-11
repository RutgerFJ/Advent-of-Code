def part_one(inp):
    digits = []

    for line in inp:
        all_line_digits = ''.join([i for i in line if i.isdigit()])
        line_value = int(all_line_digits[0] + all_line_digits[-1])
        digits.append(line_value)

    return sum(digits)


def part_two(inp):
    digit_dict = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    file_digits = []
  
    for line in inp:
        line_digits = ''

        for i, char in enumerate(line):
            if char.isdigit():
                line_digits += char
            else:
                for word in digit_dict:
                    if word == line[i:i+len(word)]:
                        line_digits += digit_dict[word]

        file_digits.append(int(line_digits[0]+line_digits[-1]))

    return sum(file_digits)


if __name__ == '__main__':
    with open('./2023/Day 1/input.txt', 'r') as f:
        content = [line.strip() for line in f]
    
    print(part_one(content))
    print(part_two(content))
