from math import prod


def part_one(inp):
    game_number_total = 0
    color_dict = {'red': 12, 'green': 13, 'blue': 14}
    
    for game in inp:
        valid_game = True
        hands = [hand.strip() for hand in game.strip().split(':')[1].split(';')]
        
        for hand in hands:
            for color in hand.split(','):
                number = int(color.strip().split()[0])
                color = color.strip().split()[1].strip(',').strip()
                if color_dict[color] < number:
                    valid_game = False
                    break
            
        if valid_game:
            game_number_total += int(game.strip().split(':')[0].split()[1])

    return game_number_total


def part_two(inp):
    game_power_total = 0

    for game in inp:
        color_dict = {'red': 0, 'green': 0, 'blue': 0}
        hands = [hand.strip() for hand in game.strip().split(':')[1].split(';')]

        for hand in hands:
            for color in hand.split(','):
                number = int(color.strip().split()[0])
                color = color.strip().split()[1].strip(',').strip()
                if number > color_dict[color]:
                    color_dict[color] = number
        
        game_power_total += prod(color_dict.values())

    return game_power_total


def main():
    with open('./AoC2023/Day 2/input.txt', 'r') as f:
        content = [line for line in f]

    print(part_one(content))
    print(part_two(content))


main()
