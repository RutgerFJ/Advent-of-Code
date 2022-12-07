from collections import defaultdict


def main():
    last_dirs, keywords, directories = [], ['$', 'cd', 'dir'], defaultdict(int)
    with open('input.txt', 'r') as f:
        for x in f:
            if x.split()[-1] == '..':
                last_dirs = last_dirs[:-1]
            elif len(x.split()) > 2:
                last_dirs.append(x.split()[2])
            elif x.split()[0] not in keywords:
                for y in range(len(last_dirs)):
                    directories[tuple(last_dirs[:y + 1])] += int(x.split()[0])

    minimum = 30000000 - (70000000 - directories[('/',)])
    print(min(bits for bits in directories.values() if bits >= minimum))


main()
