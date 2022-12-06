def main():
    with open('input.txt', 'r') as f:
        data = ''.join(line.strip('\n') for line in f)
    print([x+14 for x in range(len(data)) if len(set(data[x:x+14])) == 14][0])


main()
