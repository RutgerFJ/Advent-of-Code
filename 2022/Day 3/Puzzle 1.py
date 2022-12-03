from string import ascii_letters as alphabet


def main():
    score = 0
    with open('input.txt', 'r') as f:
        reader = [x for x in f.read().rstrip('\n').split('\n')]
    for line in reader:
        found = ''
        for char in line[0:len(line)//2:]:
            if char in line[len(line)//2::] and char not in found:
                found += char
                score += alphabet.index(char) + 1
    print(score)

main()
