def part_one(inp):
    card_sums = [0.5] * len(inp)

    for x, ln in enumerate(inp):
        wins = [num for num in ln[10:40].split() if num in ln[42:].split()]
        for _ in range(len(wins)):
            card_sums[x] *= 2

    return sum(int(x) for x in card_sums)


def part_two(inp):
    won_cards = [1] * len(inp)
    
    for x, ln in enumerate(inp):
        wins = [num for num in ln[10:40].split() if num in ln[42:].split()]        
        for y in range(x + 1, x + len(wins) + 1):
            won_cards[y] += won_cards[x]
    
    return sum(won_cards)


if __name__ == '__main__':
    with open('./2023/Day 4/input.txt', 'r') as f:
        content = [line.strip() for line in f]
    
    print(part_one(content))
    print(part_two(content))
