def main():
    score_dict = {'A X': 3,
                  'B X': 1,
                  'C X': 2,
                  'A Y': 4,
                  'B Y': 5,
                  'C Y': 6,
                  'A Z': 8,
                  'B Z': 9,
                  'C Z': 7}
    score = 0
    with open('input.txt', 'r') as f:
        for line in f:
            score += score_dict.get(line[0:3])
    print(score)


main()
