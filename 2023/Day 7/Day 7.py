from collections import Counter


def get_hand_type(hand):
    type_patterns = {'5': 7,
                     '14': 6,
                     '23': 5,
                     '113': 4,
                     '122': 3,
                     '1112': 2,
                     '11111': 1}
    
    counter = Counter(hand)
    joker = counter.pop('X', 0)

    if joker == 5:
        counts = [joker]
    else:
        counts = sorted(counter.values())
        counts[-1] += joker

    return type_patterns[''.join(list(map(str, counts)))]


def part_one(inp):
    card_ranks = 'X23456789TJQKA'
    scores = []

    for hand, bid in inp:
        hand_type = get_hand_type(hand)
        card_scores = [card_ranks.index(card) for card in hand]
        score_tuple = (hand_type, *card_scores, int(bid))
        scores.append(score_tuple)

    scores.sort()

    return sum(rank * score[-1] for rank, score in enumerate(scores, start=1))


def part_two(inp):
    return part_one([(hand.replace('J', 'X'), bid) for hand, bid in inp])


if __name__ == '__main__':
    with open('./2023/Day 7/input.txt', 'r') as f:
        content = [line.split() for line in f]

    print(part_one(content))
    print(part_two(content))
