def part_one(inp):
    card_sums = {x: 0.5 for x in range(len(inp))}

    for x, game in enumerate(inp):
        win_nums = {num for num in game[10:40].split()}
        hand_nums = {num for num in game[42:].split()}

        for _ in range(len(win_nums & hand_nums)):
            card_sums[x] *= 2

    return sum(int(val) for val in card_sums.values())


def part_two(inp):
    won_cards = {x: 1 for x in range(len(inp))}

    for x, game in enumerate(inp):
        win_nums = {num for num in game[10:40].split()}
        hand_nums = {num for num in game[42:].split()}

        for y in range(x + 1, x + len(hand_nums & win_nums) + 1):
            won_cards[y] += won_cards[x]
    
    return sum(won_cards.values())


def main():
    with open('./AoC2023/Day 4/input.txt', 'r') as f:
        content = [line.strip() for line in f]
    
    print(part_one(content))
    print(part_two(content))


main()
