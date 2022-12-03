from string import ascii_letters as alphabet


def main():
    score = 0
    with open('input.txt', 'r') as f:
        reader = [l for l in f.read().rstrip('\n').split('\n')]
    for x in range(len(reader))[0::3]:
        e_1, e_2, e_3, found = reader[x], reader[x + 1], reader[x + 2], ''
        for char in e_1:
            if char not in found and char in e_2 and char in e_3:
                found += char
                score += alphabet.index(char) + 1
    print(score)


main()
