def part_one(inp):
    card_sums = {x: 0.5 for x in range(len(inp))}

    for x, ln in enumerate(inp):
        wins = [num for num in ln[10:40].split() if num in ln[42:].split()]
        for _ in wins:
            card_sums[x] *= 2

    return sum(int(val) for val in card_sums.values())


def part_two(inp):
    won_cards = {x: 1 for x in range(len(inp))}

    for x, ln in enumerate(inp):
        wins = [num for num in ln[10:40].split() if num in ln[42:].split()]
        for y in range(x + 1, x + len(wins) + 1):
            won_cards[y] += won_cards[x]
    
    return sum(won_cards.values())


def main():
    with open('input.txt', 'r') as f:
        content = [line.strip() for line in f]
    
    print(part_one(content))
    print(part_two(content))


main()
