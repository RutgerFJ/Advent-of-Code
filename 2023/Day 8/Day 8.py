from math import lcm
import re


def part_one(inp):
    moves = inp[0]
    nodes = {pos: (left, right) for pos, left, right in 
             [re.findall('[A-Z]{3}', line) for line in inp[2:]]}

    node, count = 'AAA', 0
    while node != 'ZZZ':
        node = nodes[node][moves[count % len(moves)] == 'R']
        count += 1
    
    return count


def part_two(inp):
    moves = inp[0]
    nodes = {pos: (left, right) for pos, left, right in 
             [re.findall('[A-Z]{3}', line) for line in inp[2:]]}

    a_nodes = [node for node in nodes if node[-1] == 'A']
    cycles = []
    for node in a_nodes:
        count = 0
        while not node[-1] == 'Z':
            node = nodes[node][moves[count % len(moves)] == 'R']
            count += 1
        cycles.append(count)

    return lcm(*cycles)
    

if __name__ == '__main__':
    with open('./2023/Day 8/input.txt', 'r') as f:
        content = [line.strip() for line in f]

    print(part_one(content))
    print(part_two(content))
