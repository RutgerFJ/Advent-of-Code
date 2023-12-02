from math import prod


def part_one(inp):
    game_number_total = 0
    color_dict = {'red': 12, 'green': 13, 'blue': 14}
    
    for game in inp:
        draws = game.split(': ')[1].replace(';', ',').split(', ')
        if any([color_dict[draw.split()[1]] < int(draw.split()[0]) for draw in draws]):
            continue
        else:
            game_number_total += int(game.split(':')[0].split()[1])

    return game_number_total


def part_two(inp):
    game_power_total = 0

    for game in inp:
        color_dict = {'red': 0, 'green': 0, 'blue': 0}
        draws = game.split(': ')[1].replace(';', ',').split(', ')
        for draw in draws:
            number = int(draw.split()[0])
            color = draw.split()[1]
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
