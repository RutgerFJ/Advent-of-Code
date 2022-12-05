def main():
    with open('input.txt', 'r') as f:
        data = [line.strip('\n') for line in f]

    stacks = [[ln[4 * x + 1] for ln in data if len(ln) == len(data[0])
               and ln[4 * x + 1].isalpha()] for x in range(len(data[0][1::4]))]
    moves = [ln.split(' ') for ln in data if ln.split(' ')[0] == 'move']

    for m in moves:
        to_move = stacks[int(m[3]) - 1][0:int(m[1])]
        stacks[int(m[3]) - 1] = stacks[int(m[3]) - 1][int(m[1])::]
        stacks[int(m[5]) - 1] = to_move + stacks[int(m[5]) - 1]

    top_layer = ''
    for s in stacks:
        top_layer += s[0]
    print(top_layer)


main()
