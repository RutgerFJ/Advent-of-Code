def calculate():
    h_score, m_score, outcomes, order = [1, 2, 3], [3, 0, 6], [], []
    count = 0
    for x in range(3):
        count += 1
        for y in range(3):
            outcomes.append((h_score[x] + m_score[(y - x % 3)]))
            order.append(x % 3 + 3 * y)

    elf_hands, hands = ['A', 'B', 'C'], ['X', 'Y', 'Z']
    matches = [(e, h) for e in elf_hands for h in hands]
    return order, outcomes, matches


def main():
    index_numbers, scores, combinations = calculate()

    score_dict = dict.fromkeys(combinations, 0)
    for i in index_numbers:
        score_dict.update({combinations[i]: scores[index_numbers[i]]})

    score = 0
    with open('input.txt', 'r') as f:
        for line in f:
            stripped = line.strip('\n')
            match = (stripped[0], stripped[2])
            score += score_dict.get(match)
    print(score)


main()
