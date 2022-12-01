def main():
    calories_per_elf = []
    calories = 0
    with open('elves.txt', 'r') as f:
        for line in f:
            if line != "\n":
                calories += int(line)
            else:
                calories_per_elf.append(calories)
                calories = 0
    elves_sorted = sorted(calories_per_elf)
    print(elves_sorted[-1])

main()
