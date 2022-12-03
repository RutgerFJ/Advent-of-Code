def main():
    calories_per_elf = []
    calories = 0
    with open('input.txt', 'r') as f:
        for line in f:
            if line != "\n":
                calories += int(line)
            else:
                calories_per_elf.append(calories)
                calories = 0
    print(sorted(calories_per_elf)[-3::])


main()
