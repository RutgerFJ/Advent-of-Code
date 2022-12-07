def main():
    hand_pairs = [(e, h) for e in ['A', 'B', 'C'] for h in ['X', 'Y', 'Z']]
    score_dict = dict.fromkeys(hand_pairs, 0)
    s = [[1, 2, 3][x] + [3, 0, 6][(y - x % 3)] for x in range(3) for y in range(3)]
    order = [x % 3 + 3 * y for x in range(3) for y in range(3)]

    for i in order:
        score_dict.update({hand_pairs[i]: s[order[i]]})
    with open('input.txt', 'r') as f:
        matches = [(line[0], line[2]) for line in f]
    print(sum([score_dict.get(match) for match in matches]))


main()
