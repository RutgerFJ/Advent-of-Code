def main():
    with open('input.txt', 'r') as f:
        content = [line.strip('\n\n') for line in f]

    stacks = [[line[4 * x + 1] for line in content if len(line) > 33 and
               line[4 * x + 1].isalpha()] for x in range(9)]
    moves = [line.split(' ') for line in content if len(line) in range(15, 25)]
    
    for m in moves:
        to_move = stacks[int(m[3]) - 1][0:int(m[1])]
        stacks[int(m[3]) - 1] = stacks[int(m[3]) - 1][int(m[1])::]
        stacks[int(m[5]) - 1] = to_move[::-1] + stacks[int(m[5]) - 1]

    top_layer = ''
    for s in stacks:
        top_layer += s[0]
    print(top_layer)


main()
  
