from collections import defaultdict
from math import prod


def part_one(inp):
    number = ''
    adjacent_sum = 0
    adjacent = False

    for y, line in enumerate(inp):
        for x, char in enumerate(line):
            if char.isdecimal():
                number += char

                c = ((x + ij[0], y + ij[1]) for ij in 
                     [(i, j) for i in range(-1, 2) for j in range(-1, 2)] 
                     if x + ij[0] in range(len(line)) and y + ij[1] in range(len(inp)))
                for xy in c:
                    if inp[xy[1]][xy[0]] not in '0123456789.':
                        adjacent = True

            if not char.isdecimal() or x == len(line) - 1:
                if adjacent:
                    adjacent_sum += int(number)
                    adjacent = False
                number = ''

    return adjacent_sum


def part_two(inp):
    number = ''
    gears = defaultdict(list)
    gear = False

    for y, line in enumerate(inp):
        for x, char in enumerate(line):
            if char.isdecimal():
                number += char

                c = ((x + ij[0], y + ij[1]) for ij in 
                     [(i, j) for i in range(-1, 2) for j in range(-1, 2)] 
                     if x + ij[0] in range(len(line)) and y + ij[1] in range(len(inp)))
                for xy in c:
                    if inp[xy[1]][xy[0]] == '*':
                        gear = (xy[1], xy[0])

            if not char.isdecimal() or x == len(line) - 1:
                if gear:
                    gears[gear].append(int(number))
                    gear = False
                number = ''

    return sum(prod(gears[gear]) for gear in gears.keys() if len(gears[gear]) == 2)


def main():
    with open('input.txt', 'r') as f:
        content = [line.strip() for line in f]

    print(part_one(content))
    print(part_two(content))


main()
