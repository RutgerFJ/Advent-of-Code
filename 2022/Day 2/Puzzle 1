def calculate():
    h_score, m_score, outcomes, order = [1, 2, 3], [3, 0, 6], [], []
    for x in range(3):
        for y in range(3):
            outcomes.append((h_score[x] + m_score[(y - x % 3)]))
            order.append(x % 3 + 3 * y)

    elf_hands, hands = ['A', 'B', 'C'], ['X', 'Y', 'Z']
    matches = [(e, h) for e in elf_hands for h in hands]

    score_dict = dict.fromkeys(matches, 0)
    for i in order:
        score_dict.update({matches[i]: outcomes[order[i]]})
    return score_dict


def main():
    score_dictionary = calculate()
    score = 0
    with open('input.txt', 'r') as f:
        for line in f:
            stripped = line.strip('\n')
            match = (stripped[0], stripped[2])
            score += score_dictionary.get(match)
    print(score)


main()
