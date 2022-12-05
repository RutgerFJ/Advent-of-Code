def main():
    with open('input.txt', 'r') as f:
        data = [line.strip('\n') for line in f]

    stax = [[ln[4 * x + 1] for ln in data if len(ln) == len(data[0])
             and ln[4 * x + 1].isalpha()] for x in range(len(data[0][1::4]))]
    moves = [ln.split(' ') for ln in data if ln.split(' ')[0] == 'move']

    for m in moves:
        stax[int(m[5])-1] = stax[int(m[3])-1][0:int(m[1])] + stax[int(m[5])-1]
        stax[int(m[3])-1] = stax[int(m[3])-1][int(m[1])::]

    print(''.join([s[0] for s in stax]))


main()
