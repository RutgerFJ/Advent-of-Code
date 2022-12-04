from collections import Counter


def main():
    with open('input.txt', 'r') as f:
        content = [x.strip().split(' ') for x in f]

    strings = ['' for x in range(12)]
    for line in content:
        for x in range(12):
            strings[x] += line[0][x]

    gamma, epsilon = '', ''
    for i in range(12):
        gamma += Counter(strings[i]).most_common(1)[0][0]
        if Counter(strings[i]).most_common(1)[0][0] == '1':
            epsilon += '0'
        else:
            epsilon += '1'
    print(int(gamma, 2) * int(epsilon, 2))


main()
