def main():
    score_dict = {'A X': 4,
                  'B X': 1,
                  'C X': 7,
                  'A Y': 8,
                  'B Y': 5,
                  'C Y': 2,
                  'A Z': 3,
                  'B Z': 9,
                  'C Z': 6}
    score = 0
    with open('input.txt', 'r') as f:
        for line in f:
            score += score_dict.get(line[0:3])
    print(score)


main()
