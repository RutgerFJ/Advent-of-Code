def main():
    with open('input.txt', 'r') as f:
        content = [line.strip('\n').split(',') for line in f]

    matches = 0
    for line in content:
        split_1, split_2 = line[0].split('-'), line[1].split('-')
        e1 = [x for x in range(int(split_1[0]) - 1, int(split_1[1]))]
        e2 = [x for x in range(int(split_2[0]) - 1, int(split_2[1]))]
        if min(e1) in e2 or max(e1) in e2 or min(e2) in e1 or max(e2) in e1:
            matches += 1
    print(matches)


main()
  
